# tag 모두 불러옴
# 한번에 열고닫는 태그
from html_tags.tag import tag
# 열기만 하는 태그
from html_tags.open_tag import open_tag
# 열고 닫으면서 내용 채우는 태그
from html_tags.open_close_tag import open_close_tag

# doctype html 선언
# open_tag 태그
doc_html = open_tag("!DOCTYPE",types=['"html"'])


# meta charset 태그
# tag
meta_charset = tag("meta",types=["charset"],values=['"UTF-8"'])

# meta name content 태그
# tag
meta_name_content = tag("meta",types=["name","content"],values=['"viewport"','"width=device-width, initial-scale=1.0"'])


# h1 태그
# open_close_tag
h1 = open_close_tag("h1",childrens=["제목"])
# p 태그
# open_close_tag
p = open_close_tag("p",childrens=["내용"])

# body 태그
# open_close_tag
body = open_close_tag("body",childrens=[h1, p])

# head 태그
# open_close_tag
head = open_close_tag("haed", childrens=[meta_charset, meta_name_content])


# html태그
html = open_close_tag("html",childrens=[head,body])


# 작성
with open("indexB.html","w",encoding="utf-8")as file:
    file.write(f"{doc_html}{html}")