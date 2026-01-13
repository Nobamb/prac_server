// 제작할 태그들의 구조의 집합

// 태그 관련 함수들 가져옴
import tag from "../html_tags/tag.js";
import openTag from "../html_tags/openTag.js";
import openCloseTag from "../html_tags/openCloseTag.js";


// h1
// 열고 닫는 태그
// 속성은 class, id
// 속성값은 "title","h1Title"
// 내용은 "제목"
const h1 = openCloseTag("h1",["class","id"],['title',"h1Title"],["제목"])

// p
// 열고 닫는 태그
// 속성은 class, id
// 속성값은 "content","pContent"
// 내용은 "내용"
const p = openCloseTag("p",["class","id"],['content',"pContent"],["내용"])

// br
// 태그 하나로 열고 닫는 태그

const br = tag("br")

// doctype
// 열기만 하는 태그
// 속성명 html
const doctype = openTag("!DOCTYPE",["html"])


// meta데이터 태그

// charset 관련
// 열기만 하는 태그
// 속성명 charset
// 속성값 "UTF-8"
const metaChar = tag("meta",["charset"],["UTF-8"])

// meta name, content 관련
// 열기만 하는 태그
// 속성명 name,content
// 속성값 "viewport", "width=device-width, initial-scale=1.0"
const metaView = tag("meta",["name","content"],["viewport","width=device-width, initial-scale=1.0"])


// title 태그
// 열고 닫는 태그
// 내용은 테스트
const title = openCloseTag("title",[],[],["테스트"])

// head
// 열고 닫는 태그
// 메타 태그와 제목 태그를 children으로 받음
const head = openCloseTag("head",[],[],[metaChar,metaView,title])

// body
// 열고 닫는 태그
// h1, p와 같은 값들을 children으로 받음
const body = openCloseTag("body",[],[],[h1, br, p])


// html
// 열고 닫는 태그
// 속성명 lang
// 속성값 ko
// body, head 태그를 children으로 받음
const html = openCloseTag("html",["lang"],["ko"],[head, body])

// export
// html, doctype 내보내기
export {html, doctype}