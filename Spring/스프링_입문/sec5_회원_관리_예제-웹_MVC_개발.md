# 회원 관리 예제 - 웹 MVC 개발
## 회원 웹 기능 - 홈 화면 추가
접속할 때 스프링 컨테이너에서 컨트롤러를 먼저 찾고, 없으면 정적 컨텐츠를 찾는다. `@GetMapping('/')`이 존재하므로 index.html은 무시된다.
## 회원 웹 기능 - 등록, 조회
`@GetMapping`과 `@PostMapping` 에서 Get과 Post는 HTTP Method이다.
- GET: 조회
- POST: 데이터 저장
