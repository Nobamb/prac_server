import openTag from "./tag.js";

// 열고 닫는 태그를 제작하는 함수
// 클로저 형식 함수
// 첫번째 파라마터 : tagName (태그이름)
// 두번째 파라미터 : types (속성명, 배열형식)
// 세번째 파라미터 : values (속성값, 배열형식)
// 네번째 파라미터 ㅣ chidren(태그 내부에 들어가는 내용, 배열 형식)


// types, values, children 모두 기본값 빈 배열
const openCloseTag = (tagName, types = [], values = [], children=[])=> {

    // 시작 태그
    // openTag 함수 import
    const tagStart = openTag(tagName, types, values);

    // 닫는 태그
    const tagEnd = `</${tagName}>`

    // 들어갈 내용
    let content = ''
    // 클로저 함수를 통해
    // content에 들어갈 내용 추가
    const childrenPlus = (children) => {

        // children 분해 
        children.forEach(element => {
            // content에 element 추가
            content += element;
        });
    }

    // content에 내용 추가
    childrenPlus(children);

    // 최종 값 생성
    const result = tagStart + content + tagEnd;

    // result 반환
    return result;

}