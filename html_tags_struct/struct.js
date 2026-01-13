// 제작할 태그들의 구조의 집합

// 태그 관련 함수들 가져옴
import tag from "../html_tags/tag.js";
import openTag from "../html_tags/openTag.js";
import openCloseTag from "../html_tags/openCloseTag.js";

// 클래스 형식으로 지정
class Struct {
  // h1
  // 열고 닫는 태그
  // 속성은 class, id
  // 속성값은 "title","h1Title"
  // 내용은 "제목"
  static h1 = openCloseTag(
    "h1",
    ["class", "id"],
    ["title", "h1Title"],
    ["제목"]
  );

  // p
  // 열고 닫는 태그
  // 속성은 class, id
  // 속성값은 "content","pContent"
  // 내용은 "내용"
  static p = openCloseTag(
    "p",
    ["class", "id"],
    ["content", "pContent"],
    ["내용"]
  );

  // br
  // 태그 하나로 열고 닫는 태그

  static br = tag("br");
  // meta데이터 태그

  // charset 관련
  // 열기만 하는 태그
  // 속성명 charset
  // 속성값 "UTF-8"
  static metaChar = tag("meta", ["charset"], ["UTF-8"]);

  // meta name, content 관련
  // 열기만 하는 태그
  // 속성명 name,content
  // 속성값 "viewport", "width=device-width, initial-scale=1.0"
  static metaView = tag(
    "meta",
    ["name", "content"],
    ["viewport", "width=device-width, initial-scale=1.0"]
  );

  // title 태그
  // 열고 닫는 태그
  // 내용은 테스트
  static title = openCloseTag("title", [], [], ["테스트"]);

  // head
  // 열고 닫는 태그
  // 메타 태그와 제목 태그를 children으로 받음
  static head = openCloseTag(
    "head",
    [],
    [],
    [this.metaChar, this.metaView, this.title]
  );

  // body
  // 열고 닫는 태그
  // h1, p와 같은 값들을 children으로 받음
  static body = openCloseTag("body", [], [], [this.h1, this.br, this.p]);

  // 정적 속성 doctype, html

  // doctype
  // 열기만 하는 태그
  // 속성명 html
  static doctype = openTag("!DOCTYPE", ["html"]);

  // html
  // 열고 닫는 태그
  // 속성명 lang
  // 속성값 ko
  // body, head 태그를 children으로 받음
  static html = openCloseTag("html", ["lang"], ["ko"], [this.head, this.body]);

  //   기본값 자동완성
  static defualtStruct = this.doctype + this.html;
}


// 변경 테스트
// static 값을 변경하여 값이 제대로 바뀌는 지 테스트
Struct.h1 = openCloseTag(
  "h1",
  ["class", "id"],
  ["newTitle", "newH1Title"],
  ["변경된 제목"]
);


// 내보내기
export default Struct;
