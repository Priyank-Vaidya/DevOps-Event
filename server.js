const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Serve the HTML file
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Handle registration
app.post('/register', (req, res) => {
    const { name, email, designation } = req.body;
    console.log('New registration:', { name, email, designation });
    // Here, you can add the registration data to your database or perform any other action
    // For simplicity, let's just send a success response
    res.status(200).send('Registration successful');
});

app.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}`);
});
