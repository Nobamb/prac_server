# 클래스 제작


# 열고 닫는 태그가 하나에 모여있는 태그

# 클로저 진행
def tag(tag_name,types):
    # 이름 지정(은닉 변수)
    tag_start = f"<{tag_name} "
    
    # type들 추가(클로저)
    def type_plus(tagOpen, types):
        tag = tagOpen
        # 배열을 하나씩 나눔
        for type_name in types:
            # 타입명을 tag에 추가
            tag += f"{type_name} "
        # 닫는 태그 지정
        tag += "/>"
        # tag 반환
        return tag
    
    # type추가
    tag = type_plus(tag_start, types)
    
    # tag 출력
    return tag

# meta 태그
meta = tag("meta",["type1","type2"])

print(meta)



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
with open("index2.html", "w") as index:
    index.write(
        '<!DOCTYPE html><html lang = "ko"><head><meta charset="UTF-8"><title>문서</title></head><body><h1>문서 작성</h1></body></html>'
    )
