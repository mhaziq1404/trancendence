const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');

const app = express();
const port = 3000;

app.use(bodyParser.json());

const secretKey = 'your_secret_key'; // Replace with a secure secret key

// Endpoint to generate JWT token
app.post('/generateToken', (req, res) => {
  const { username } = req.body;

  // Generate JWT token
  const token = jwt.sign({ username }, secretKey, { expiresIn: '1h' });

  res.json({ token });
});

// Endpoint to validate JWT token
app.post('/validateToken', (req, res) => {
  const { token } = req.body;

  jwt.verify(token, secretKey, (err, decoded) => {
    if (err) {
      res.status(401).json({ message: 'Invalid token' });
    } else {
      res.json({ message: 'Token is valid', decoded });
    }
  });
});

app.listen(port, () => {
  console.log(`JWT service listening at http://localhost:${port}`);
});
