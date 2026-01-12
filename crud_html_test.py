# 클래스 제작


# 열고 닫는 태그가 하나에 모여있는 태그

# 클로저 진행
# 한번에 열고 닫는 태그
def tag(tag_name,types,values):
    # 이름 지정(은닉 변수)
    tag_start = f"<{tag_name}"
    
    # type들 추가(클로저)
    def type_plus(tagOpen, types, values):
        tag = tagOpen
        # 배열을 하나씩 나눔
        for index,type_name in enumerate(types):
            # 타입명을 tag에 추가
            tag += f" {type_name}={values[index]}"
        # 닫는 태그 지정
        tag += "/>"
        # tag 반환
        return tag
    
    # type추가
    tag = type_plus(tag_start, types, values)
    
    # tag 출력
    return tag


# 열기만 하는 태그
def open_tag(tag_name, types):
    # 시작 태그 작성
    tag_start = f"<{tag_name}"
    # types를 토대로 클로저 함수 생성
    def type_plus(tag_start, types):
        # 시작 태그 지정
        tag = tag_start
        # tag에 type들 모두 대입
        for type_name in types:
            tag += f" {type_name}"
        # 모두 더하면 닫기
        tag += ">"
        # tag 반환
        return tag
    
    # type_plus 실행
    tag = type_plus(tag_start, types)
    # tag return
    return tag
    
    
    
# 열고 닫는 태그
def open_close_tag(tag_name, types, childrens):
    # 태그 열기
    tag_start = f"<{tag_name}"
    
    # type 추가
    def type_plus(tag_start, types):
        # tag 지정
        tag = tag_start
        # type들 모두 추가
        for type_name in types:
            tag += f" {type_name}"
        
        # type들 모두 추가한 후,
        # 닫아버리기(시작 태그 기준)
        tag += ">"
        return tag
    # 시작 태그 지정
    open_tag = type_plus(tag_start,types)
    
    
    # 태그 내의 result 지정
    # children 값들 모두 추가
    result_init = ""
    
    # 배열 childrens을 분해하여
    # result에 추가
    def children_plus(result_init, childrens):    
        # open_tag에 children 배열들 모두 추가
        # children으로 나눔
        for children in childrens:
            # children 추가
            result_init += children
        # children 값들 모두 return
        return result_init
    
    # 결과들 대입
    result = children_plus(result_init, childrens)
    
    
    # close_tag 지정
    close_tag = f"</{tag_name}>"
    
    
    # 총 태그 지정
    total_tag = open_tag + result + close_tag
    
    # 출력
    return total_tag
    
    
# meta 태그
meta = tag("meta",["type1","type2"], ["value1","value2"])

print(meta)

# "!DOCTYPE html" 태그(열기만 함)
doc_html = open_tag("!DOCTYPE", ["html"])

print(doc_html)

# html 태그
html = open_close_tag("html",[],[])

# 출력
print(html)


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
