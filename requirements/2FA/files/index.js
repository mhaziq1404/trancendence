const express = require('express');
const bodyParser = require('body-parser');
const speakeasy = require('speakeasy');
const nodemailer = require('nodemailer');

const app = express();
const port = 3001;

app.use(bodyParser.json());

// Configure your email transport
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'your-email@gmail.com',
    pass: 'your-email-password'
  }
});

// Generate a 2FA secret
app.post('/generate-secret', (req, res) => {
  const secret = speakeasy.generateSecret({ length: 20 });
  res.json({ secret: secret.base32 });
});

// Verify a 2FA token
app.post('/verify-token', (req, res) => {
  const { token, secret } = req.body;
  const verified = speakeasy.totp.verify({
    secret: secret,
    encoding: 'base32',
    token: token
  });
  res.json({ verified });
});

// Send a 2FA token via email
app.post('/send-token', (req, res) => {
  const { email, secret } = req.body;
  const token = speakeasy.totp({ secret: secret, encoding: 'base32' });

  const mailOptions = {
    from: 'your-email@gmail.com',
    to: email,
    subject: 'Your 2FA Code',
    text: `Your 2FA code is ${token}`
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      return res.status(500).json({ error });
    }
    res.json({ message: 'Token sent' });
  });
});

app.listen(port, () => {
  console.log(`2FA server listening at http://localhost:${port}`);
});

