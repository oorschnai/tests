const http = require('node:http');

const port = Number(process.env.PORT || 8080);
const server = http.createServer((request, response) => {
  const path = new URL(request.url, 'http://localhost').pathname;
  const found = path === '/';
  response.writeHead(found ? 200 : 404, { 'Content-Type': 'text/html; charset=utf-8' });
  response.end(found
    ? "<!doctype html><html lang='en'><title>Node.js</title><h1>Hello from Node.js!</h1></html>"
    : 'Not found');
});

server.listen(port, '0.0.0.0', () => {
  console.log(`Listening on 0.0.0.0:${port}`);
});
