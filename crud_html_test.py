# 클래스 제작


# 열고 닫는 태그가 하나에 모여있는 태그
from html_tags.tag import tag
from html_tags.open_tag import open_tag
from html_tags.open_close_tag import open_close_tag


# meta 태그
meta = tag("meta", ["type1", "type2"], ["value1", "value2"])

# 연습 태그
practice_tag = tag("tag", ["tag1","tag2"],[])

# 연습 태그2
practice_tag2 = tag("tag", ["tag1","tag2"])

# 출력
print(meta)
print(practice_tag)
print(practice_tag2)


# "!DOCTYPE html" 태그(열기만 함)
doc_html = open_tag("!DOCTYPE", ["html"], [])
# 연습태그
practice_tag = open_tag("tag",["tag1","tag2"])
# 출력
print(doc_html)
print(practice_tag)


# html 태그
html = open_close_tag("html")

# 출력
print(html)

# 테스트
body = open_close_tag("body",childrens=["안녕"])
# 테스트2
tag1 = open_close_tag("tag1",childrens=["태그1"],types=["tag1"])
# 테스트3
tag2 = open_close_tag("tag2",childrens=["태그2"],types=["tag1"],values=["value1"])

# 출력1
print(body)
# 출력2
print(tag1)
# 출력3
print(tag2)


# 필요한 태그
# "!DOCTYPE html" : OpenTag
# html : OpenCloseTag
# head : OpenCloseTag
# body : OpenCloseTag


# # 테스트
# # "!DOCTYPE html"
# doctype_html = OpenTag("!DOCTYPE html")

# # 출력
# print(doctype_html.open)

# # img
# img = Tag("img")

# # 출력
# print(img.tag)

# # html
# html = OpenCloseTag("html")

# # 출력
# # open
# print(html.open)
# # close
# print(html.close)


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
with open("index3.html", "w") as index:
    index.write(
        f'<!DOCTYPE html><html lang = "ko"><head><meta charset="UTF-8"><title>문서</title></head><body>{meta}<h1>문서 작성</h1></body></html>'
    )
