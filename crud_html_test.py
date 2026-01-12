# 클래스 제작

# 열고 닫는 태그가 하나에 모여있는 태그
class Tag():
  def __init__(self, tag_name):
    self.tag = f"<{tag_name} />"

# 여는 태그만 있는 태그
class OpenTag:
  # 생성자 생성
  def __init__(self, tag_name):
    self.open = f"<{tag_name}>"

# Tag 오버라이드(닫는 태그 추가)
class OpenCloseTag(OpenTag):
  
  def __init__(self, tag_name):
     super().__init__(tag_name)
     self.close = f"</{tag_name}>"


# 테스트
# "!DOCTYPE html"
doctype_html = OpenTag("!DOCTYPE html") 

# 출력
print(doctype_html.open)

# img
img = Tag("img")

# 출력
print(img.tag)

# html
html = OpenCloseTag("html")

# 출력
# open
print(html.open)
# close
print(html.close)



# # 객체 생성하기
# # html 관련(최상위) 태그
# html = {
#     # doctype지정
#     "doctype": "<!DOCTYPE html>",
#     # html 여는 태그
#     "open": "<html>",
#     # html 닫는 태그
#     "close": "</html>",
# }

# # body 관련 태그
# body = {
#     # body 여는 태그
#     "open": "<body>",
#     # body 닫는 태그
#     "close": "</body>",
# }

# # head 관련 태그
# head = {
#     # head 여는 태그
#     "open": "<head>",
#     # head 닫는 태그
#     "close": "</head>",
# }

# # title 관련 태그

# title = {
#     # title 여는 태그
#     "open": "<title>",
#     # title 닫는 태그
#     "close": "</title>",
# }



# 파이썬의 crud를 활용하여
# html 작성해보기
with open("index2.html", "w") as index:
    index.write(
        '<!DOCTYPE html><html lang = "ko"><head><meta charset="UTF-8"><title>문서</title></head><body><h1>문서 작성</h1></body></html>'
    )
