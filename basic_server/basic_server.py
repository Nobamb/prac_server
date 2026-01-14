# 태그 가져오기
from html_tags.tag import tag
from html_tags.open_tag import open_tag
from html_tags.open_close_tag import open_close_tag


# 기존에 만들어놓은 html_tags를 활용하여
# 파이썬의 서버 방식을 통해 
# 간단한 웹 서버 제작해보기

# httpserver, basehttprequesthandler 임포트하기
from http.server import HTTPServer,BaseHTTPRequestHandler

# basehttprequesthandler를 상속하여
# WebServer라는 클래스 정의
class WebServer(BaseHTTPRequestHandler):
    # do_GET 메서드
    def do_GET(self):
        # 응답 코드 200 먼저 제작
        self.send_response(200)
        # 헤더 보내기
        # content-type : text/html
        # charset : utf-8
        self.send_header('Content-type','text/html; charset=utf-8')
        # header 마무리
        self.end_headers()
        # doctype 설정
        # open_tag 사용
        # html 타입만 지정
        doctype = open_tag('!DOCTYPE',types=['html'])
        # meta 태그 설정
        # meta_charset 속성
        # open_tag 사용
        # 속성명은 charset
        # charset 속성값은 utf-8
        meta_charset = open_tag('meta',types=['charset'],values=['utf-8'])
        # meta_viewport 태그 설정
        # open_tag 사용
        # 속성명 : name, content
        # 속성값 : viewport, width=device-width, initial-scale = 1.0
        meta_viewport = open_tag('meta',types=['name','content'],values=['viewport','width=device-width, initial-scale=1.0'])
        # title 태그 설정
        # open_close_tag 사용
        # 제목 server로 웹페이지 내용 출력
        title = open_close_tag('title',childrens=["server로 웹페이지 내용 출력"])
        # head 태그 설정
        head = open_close_tag('head',childrens=[meta_charset, meta_viewport, title])
        # h1 설정
        # open_close_tag 사용
        # 서버 페이지 테스트라는 내용 출력
        h1 = open_close_tag('h1',childrens=["서버 페이지 테스트"])
        # p 설정
        # open_close_tag 사용
        # 페이지 잘 만들었는지 테스트 라는 내용 출력
        p = open_close_tag('p',childrens=["페이지 잘 만들었는지 테스트"])
        # body 설정
        # open_close_tag 사용
        body = open_close_tag('body',childrens=[h1, p])
        # html 태그 설정
        # open_close_tag 사용
        # lang 속성 추가
        # 속성값은 ko
        html = open_close_tag('html',types=['lang'],values=['ko'],childrens=[head,body])
        
        # 전체 값들 지정
        # doctype + html
        result = doctype + html
        # 서버에 보여줌
        # write에 값을 집어넣고, encoding하기(utf-8)
        self.wfile.write(result.encoding("utf-8"))
        
        
# http 설정
# server로 생정
# 첫번째 파라미터는
# 튜플형식으로, ("",8000)
# 첫번째는 ip 지정, ""는 모든 ip 허용
# 두번째는 포트 지정, 8000이면 8000번 포트
# 두번째 파라미터는
# webserver 클래스 가져옴
# 자동으로 do_get 메서드 사용하기 위해
http = HTTPServer(("",8000),WebServer)

# http 실행
# serve_forever
http.serve_forever()