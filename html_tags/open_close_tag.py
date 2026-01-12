# 열고 닫는 태그
def open_close_tag(tag_name,  childrens=[], types=[], values=[]):
    # 태그 열기
    tag_start = f"<{tag_name}"

    # type 추가
    def type_plus(tag_start, types,values):
        # tag 지정
        tag = tag_start
        # 만약에 values가 list면서 빈배열이 아닐때
        if type(values) and values != []:
            # type들 모두 추가
            for index, type_name in enumerate(types):
                # type 및 values의 인덱스에 해당하는 값들 추가
                tag += f" {type_name}={values[index]}"
        # values가 list면서 빈배열일때
        if type(values) and values == []:
            # type들 모두 추가
            for type_name in types:
                # tag에 type 모두 대입
                tag += f" {type_name}"

        # type들 모두 추가한 후,
        # 닫아버리기(시작 태그 기준)
        tag += ">"
        return tag

    # 시작 태그 지정
    open_tag = type_plus(tag_start, types,values)

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
