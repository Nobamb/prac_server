import openTag from "./openTag.js";

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


// 테스트
// 속성과 속성값이 있는 태그
const testTag1 = openCloseTag("div",["class", "id"], ["container","main"], ["안녕하세요","<p>반갑습니다</p>"]);
// 속성만 있는 태그(속성값 x)
const testTag2 = openCloseTag("div",["class", "id"], [], ["내용이 있는 태그"]);
// 속성, 속성값이 없는 태그
const testTag3 = openCloseTag("div", [], [], ["내용이 있는 태그"]);
// 내용이 있는 태그
const testTag4 = openCloseTag("p", [], [], ["안녕하세요! 내용이 있는 태그입니다."]);
// 모두 없는 태그
const testTag5 = openCloseTag("script")

// 출력
console.log(testTag1);
console.log(testTag2);
console.log(testTag3);
console.log(testTag4);
console.log(testTag5);
