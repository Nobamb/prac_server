const http = require('http');

const hostname = 'localhost'; // 내 컴퓨터
const port = 8000; // 포트 번호

const server = http.createServer((req, res) => {
  if (req.method === 'GET') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html; charset=utf-8');

    const message = '<h1>안녕하세요! Node.js 서버입니다.</h1>';
    res.end(message);
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

