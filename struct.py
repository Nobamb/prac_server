practice = {
    "left_angle_bracket": "<",
    "right_angle_bracket": ">",
    "tag_name": "",
    "close_tag_slash": "/",
    "children_elements": [],
}

# <공욱재>나야</공욱재>
practice["tag_name"] = "공욱재"
result = f"{practice["left_angle_bracket"]} {practice["tag_name"]} {practice["right_angle_bracket"]}나야{practice["left_angle_bracket"]} {practice["close_tag_slash"]} {practice["tag_name"]} {practice["right_angle_bracket"]}"

# 출력
print(result)


# 다른 태그명으로 해보기
practice["tag_name"] = "돈까스"

result = f"{practice["left_angle_bracket"]} {practice["tag_name"]} {practice["right_angle_bracket"]}나야{practice["left_angle_bracket"]} {practice["close_tag_slash"]} {practice["tag_name"]} {practice["right_angle_bracket"]}"

# 출력
print(result)


# 다른 태그명으로 해보기
practice["tag_name"] = "제육볶음"

# 제육볶음은 인라인 태그
result = f"{practice["left_angle_bracket"]} {practice["tag_name"]} {practice["close_tag_slash"]} {practice["right_angle_bracket"]}"

# 출력
print(result)


# 동일
# print("<" + "공욱재" + ">" + "나야" + "<" + "/" + "공욱재" + ">")