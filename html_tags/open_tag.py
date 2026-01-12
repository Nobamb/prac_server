# 열기만 하는 태그
def open_tag(tag_name, types=[], values=[]):
    # 시작 태그 작성
    tag_start = f"<{tag_name}"

    # types를 토대로 클로저 함수 생성
    def type_plus(tag_start, types, values):
        # 시작 태그 지정
        tag = tag_start
        # 만약, values가 리스트면서 값이 없다면
        # tag에 type들 모두 대입하면서
        # values 적용
        if type(values) == list and values != []:
            for index, type_name in enumerate(types):
                tag += f" {type_name}={values[index]}"
        # values가 리스트면서 값이 있다면
        # values가 빈배열이 맞다면
        elif type(values) == list and values == []:
            for type_name in types:
                tag += f" {type_name}"
        # 모두 더하면 닫기
        tag += ">"
        # tag 반환
        return tag

    # type_plus 실행
    tag = type_plus(tag_start, types, values)
    # tag return
    return tag