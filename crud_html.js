// 파일 제작
// fs 모듈 불러오기
import fs from 'node:fs/promises';
// tag 관련 모듈들 모두 가져오기
import tag from "./html_tags/tag.js"
import openTag from "./html_tags/openTag.js"
import openCloseTag from "./html_tags/openCloseTag.js"



// 파일을 작성하는 함수 생성
const createFile = async (filename, fileContent)=> {

    try{

        // 테스트
        console.log("동작 테스트")
        // crud를 통해 파일 작성 연습
        await fs.writeFile(filename, fileContent)
        console.log('파일 작성 완료')

    }
    catch(error){
        console.error("파일 에러 발생",error)
        throw error;
    }
    finally{
        console.log("파일 작성 종료")
    }


}

// 테스트
// h1 태그에 class, id 속성 추가
// class : "title"
// id : "h1Title"
// children : "안녕하세요"

const h1 = openCloseTag("h1",["class","id"],["title","h1Title"],["안녕하세요"])


// 실행
await createFile("indexBC.html",h1)