const express = require('express');
const app = express();
const port = process.env.PORT || 3000;
const QRCode = require('qrcode');


app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

app.get('/generate_qr', async (req, res) => {
  try {
    const url = 'http://10.0.0.16:8000/trigger-relay'; // This could be dynamic based on query params
    const qrCodeImage = await QRCode.toDataURL(url);
    res.send(`<img src="${qrCodeImage}"/>`); // Sends QR code as an image
  } catch (error) {
    res.status(500).send('Error generating QR code');
  }
});