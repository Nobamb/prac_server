// 클로저 형식의 함수
// 태그 하나로 열고 닫는 함수

// html 태그를 만들어주는 코드
// 첫번째 파라미터 : 태그이름
// 두번째  파라미터 : 속성 이름(배열로 받음)
// 세번째 파라미터 : 속성 내용(배열로 받음)
// types, values 둘 다 기본값 빈 배열
// 아예 속성을 안넣고 태그를 만들수있기에


const tag = (tagName, {types=[],values=[]}={}) => {
    // 시작 태그
    let tag = `<${tagName}`

    // 클로저 함수
    // 속성에 속성값을 추가
    const typePlus = (types, values)=> {
    

        // 속성들을 분해함
        types.forEach((element,index) => {
            
            // 만약에 values가 배열 형식이면서
            // 빈배열이 아닐 때
            if(typeof values === 'object' && values.length > 0){
                // 속성명에 "="를 붙이면서 
                // tag에 속성명과 속성 값을 넣어줌
                tag += ` ${element}="${values[index]}"`
            }
            // 만약에 values가 배열 형식이면서
            // 빈배열이 아닐 때
            else if(typeof values === 'object' && values.length <= 0){

                // tag에 속성명과 속성 값을 넣어줌
                tag += ` ${element}`

            }


        })
        
        // 태그 마무리
        tag += `/>`
        
    };
    // typePlus 함수 실행
    typePlus(types, values)

    // 최종 태그 반환

    return tag;


}

// // 태그 생성 테스트
// const testTag1 = tag("div",["class", "id"], ["container","main"])
// // 태그 생성 테스트 2
// const testTag2 = tag("div")


// // 출력
// console.log(testTag1)
// console.log(testTag2)

// export
export default tag