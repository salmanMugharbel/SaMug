const http = require('http');
const fs = require('fs');
const path = require('path');

// Create a server to serve HTML and handle API requests
const server = http.createServer((req, res) => {
  if (req.url === '/') {
    // Serve the HTML file
    fs.readFile(path.join(__dirname, 'index.html'), (err, data) => {
      if (err) {
        res.writeHead(500);
        res.end('Error loading the page');
      } else {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
      }
    });
  } else if (req.url.startsWith('/calculate')) {
    const urlParams = new URLSearchParams(req.url.split('?')[1]);
    const num1 = parseFloat(urlParams.get('num1'));
    const num2 = parseFloat(urlParams.get('num2'));
    const operation = urlParams.get('operation');
    let result;

    // Perform the calculation based on operation
    switch (operation) {
      case 'add':
        result = num1 + num2;
        break;
      case 'subtract':
        result = num1 - num2;
        break;
      case 'multiply':
        result = num1 * num2;
        break;
      case 'divide':
        result = num2 !== 0 ? num1 / num2 : 'Error: Division by zero';
        break;
      default:
        result = 'Invalid operation';
    }

    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ result }));
  }
});

// Start the server
server.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
