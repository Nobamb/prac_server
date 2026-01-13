// 클로저 형식의 함수
// 태그 하나로 열고 닫는 함수

// html 태그를 만들어주는 코드
// 첫번째 파라미터 : 태그이름
// 두번째  파라미터 : 속성 이름(배열로 받음)
// 세번째 파라미터 : 속성 내용(배열로 받음)

const tag = (tagName, types,values) => {
    // 시작 태그
    let tagStart = `<${tagName}`

    // 클로저 함수
    // 속성에 속성값을 추가
    const typePlus = (types, values)=> {
    

        // 속성들을 분해함
        types.forEach(element,index => {
            
            // 만약에 values가 배열 형식이면서
            // 빈배열이 아닐 때
            if(typeof values === 'object' && values.length > 0){
                // 속성명에 "="를 붙이면서 
                // tagStart에 속성명과 속성 값을 넣어줌
                tagStart += ` ${element}="${values[index]}"`
            }
            // 만약에 values가 배열 형식이면서
            // 빈배열이 아닐 때
            else if(typeof values === 'object' && values.length <= 0){

                // tagStart에 속성명과 속성 값을 넣어줌
                tagStart += ` ${element}`

            }


        })
        
        // 태그 마무리
        tagStart += `>`
        
    };
    // typePlus 함수 실행
    typePlus(types, values)

    // 태그 닫기
    tagEnd = `</${tagName}>`

    // 최종 태그 반환
    result = tagStart + tagEnd

    return result;


}





// export
export default tag