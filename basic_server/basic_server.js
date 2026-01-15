// http 가져오기
import http from "http";
// 태그 가져오기
import tag from "../html_tags/tag.js";
import openTag from "../html_tags/openTag.js";
import openCloseTag from "../html_tags/openCloseTag.js";

// 서버 생성
// req, res 파라미터로 받음
const server = http.createServer((req, res) => {
  // request 요청이 GET일 때
  if (req.method === "GET") {
    // 응답에서 헤더 작성
    // 200번대 응답
    // contenttype
    // text/html; charset utf-8
    res.writeHead(200, { "content-type": "text/html; charset=utf-8" });

    // 태그 작성
    // openTag 사용
    // html 속성만
    const doctype = openTag("!DOCTYPE", ["html"]);

    // p태그
    // openCloseTag 사용
    // 내용은 서버를 통해서 웹사이트 내용이 제대로 렌더링 되는지 테스트
    const p = openCloseTag("p", {
      children: ["서버를 통해서 웹사이트 내용이 제대로 렌더링 되는지 테스트"],
    });

    // h1태그
    // openCloseTag 사용
    // 내용은 ssr 서버 테스트
    const h1 = openCloseTag("h1", { children: ["ssr 서버 테스트"] });

    // body 작성
    // openCloseTag 사용
    // h1, p를 받음
    const body = openCloseTag("body",{children:[h1, p]});

    // meta 태그들
    // meta charset
    // 속성명 charset
    // 속성값 UTF-8
    // openTag사용
    const metaCharset = openTag("meta", { types: ["charset"] });

    // meta name 및 content
    // 속성명 name/content
    // 속성값 viewport/width=device-width, initial-scale = 1.0
    const metaContent = openTag("meta", {
      types: ["name", "content"],
      values: ["viewport", "width=device-width, initial-scale:1.0"],
    });

    // title
    // openCloseTag 사용
    // 내용은 ssr테스트
    const title = openCloseTag("title", { children: ["ssr테스트"] });

    // head 작성
    // openCloseTag 사용
    // metaCharset, metaContent, title을 받음
    const head = openCloseTag("head", [metaCharset, metaContent, title]);

    // html 태그 작성
    const html = openCloseTag("html", { children: [head, body] });

    // 내보낼 값
    const result = doctype + html;

    // 표시될 값
    res.end(result);
  }
});
