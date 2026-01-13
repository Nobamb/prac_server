// 열기만 하는 코드 제작
// 클로저 함수
// DOCTYPE 선언 같은 경우 사용됨

// 첫번째 파라미터 : 태그 네임 tagName
// 두번째 파라미터 : 속성명 typeps(배열형식)
// 세번째 파라미터 : 속성값 values(배열형식)

const openTag = (tagName, types = [], values = []) => {
  // 태그
  let tag = `<${tagName}`;

  // 클로저함수
  const typePlus = (types, values) => {
    // 속성들을 분해함
    types.forEach((element, index) => {
      //만약에 types가 배열 형식이면서
      // 빈 배열이 아닐 때
      if (typeof values === "object" && values.length > 0) {
        // 속성명에 =를 붙이면서
        // 인덱스에 맞는 value값 추가
        tag += ` ${element}=${values[index]}`;
      }
      //만약에 types가 배열 형식이면서
      // 빈 배열이 아닐 때
      else if (typeof values === "object" && values.length <= 0) {
        // 속성명만 추가
        tag += ` ${element}`;
      }
    });

    // 태그 끝
    tag += `>`;
  };

  //   typePlus 함수 실행
  typePlus(types, values);

  //   태그 return
  return tag;
};


// 테스트
const testTag1 = openTag("div", ["class", "id"], ['"container"','"main"']);
const testTag2 = openTag("div");

// 출력
console.log(testTag1);
console.log(testTag2);