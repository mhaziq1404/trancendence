const express = require('express');
const bodyParser = require('body-parser');
const speakeasy = require('speakeasy');
const qrcode = require('qrcode');
const nodemailer = require('nodemailer');
require('dotenv').config();

const app = express();
app.use(bodyParser.json());

// Endpoint to generate a secret and QR code
app.post('/generate-secret', (req, res) => {
    const secret = speakeasy.generateSecret({ length: 20 });
    qrcode.toDataURL(secret.otpauth_url, (err, data_url) => {
        res.json({ secret: secret.base32, qr_code: data_url });
    });
});

// Endpoint to verify the token
app.post('/verify-token', (req, res) => {
    const { token, secret } = req.body;
    const verified = speakeasy.totp.verify({
        secret: secret,
        encoding: 'base32',
        token: token
    });

    res.json({ verified });
});

// Endpoint to send email with verification code
app.post('/send-email', async (req, res) => {
    const { email } = req.body;
    const token = speakeasy.totp({
        secret: process.env.EMAIL_SECRET,
        encoding: 'base32'
    });

    let transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: process.env.EMAIL_USER,
            pass: process.env.EMAIL_PASS
        }
    });

    let mailOptions = {
        from: process.env.EMAIL_USER,
        to: email,
        subject: 'Your Verification Code',
        text: `Your verification code is ${token}`
    };

    try {
        await transporter.sendMail(mailOptions);
        res.json({ message: 'Verification code sent' });
    } catch (error) {
        res.status(500).json({ error: error.toString() });
    }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
