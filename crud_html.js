// 파일 제작
// fs 모듈 불러오기
import fs from 'node:fs/promises';



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
        throw error;
    }
    finally{
        console.log("파일 작성 종료")
    }


}

// 실행
await createFile("indexBC.html","<h1>안녕하세요</h1>")