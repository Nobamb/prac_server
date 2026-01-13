from http.server import HTTPServer, BaseHTTPRequestHandler

# 나만의 커스텀 핸들러 (알바생) 정의
class MyHandler(BaseHTTPRequestHandler):
    # GET 요청(주문)이 들어오면 실행되는 함수
    def do_GET(self):
        # 1. 응답 코드 200 (주문 정상 처리 완료) 전송
        self.send_response(200)
        
        # 2. 헤더 전송 (이 내용은 html 텍스트라고 알려줌)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # 3. 본문 내용 전송 (바이트 형태로 인코딩 필요)
        message = "<h1>안녕하세요! 내가 만든 첫 서버입니다.</h1>"
        self.wfile.write(message.encode('utf-8'))

# 서버 설정 및 실행
PORT = 8000
httpd = HTTPServer(("", PORT), MyHandler)

print(f"커스텀 서버 시작: http://localhost:{PORT}")
httpd.serve_forever()