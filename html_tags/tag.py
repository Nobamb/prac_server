# 클로저 진행
# 한번에 열고 닫는 태그
def tag(tag_name, types=[], values=[]):
    # 이름 지정(은닉 변수)
    tag_start = f"<{tag_name}"

    # type들 추가(클로저)
    def type_plus(tagOpen, types, values):
        tag = tagOpen
        # values타입이 list면서 비어있지 않을 때
        if type(values) == list and values != []:
            # 배열을 하나씩 나눔
            for index, type_name in enumerate(types):
                # 타입명을 tag에 추가, 값도 추가
                tag += f' {type_name}="{values[index]}"'
        # values타입이 list면서 비어있을 때
        elif type(values) == list and values == []:
            # 배열을 하나씩 나눔
            for type_name in types:
                # 타입명을 tag에 추가
                tag += f" {type_name}"
        # 닫는 태그 지정
        tag += "/>"
        # tag 반환
        return tag

    # type추가
    tag = type_plus(tag_start, types, values)

    # tag 출력
    return tag
