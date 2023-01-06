# 스프링 웹 개발 기초
웹 개발의 3가지 방법
- 정적 컨텐츠: 서버 작업 x. html파일 내려주기
- MVC와 템플릿 엔진: 서버에서 프로그래밍해서 html로 내려주기 (동적 컨텐츠)
- API: 서버에서 작업하여 API로 내려주기  
</br>

## 정적 컨텐츠
<img src="https://raw.githubusercontent.com/smpark1020/tistory/master/Spring/%5B%EC%8A%A4%ED%94%84%EB%A7%81%20%EC%9E%85%EB%AC%B8%5D%20%EC%A0%95%EC%A0%81%20%EC%BB%A8%ED%85%90%EC%B8%A0/1.PNG">  

</br>

## MVC와 템플릿 엔진
MVC: Model, View, Controller - View는 화면 그리기에, Model과 Controller는 내부 처리, 비즈니스 로직에 집중  
`http://localhost:8080/helllo-mvc?name=spring`  

<img src ="https://images.velog.io/images/sewonkim/post/5a9a1966-73f9-43b5-ae21-2857b90a5144/image.png">

</br>

## API
@ ResponseBody 객체 반환
```Java
@Controller
  public class HelloController {
      @GetMapping("hello-api")
      @ResponseBody
      public Hello helloApi(@RequestParam("name") String name) {
          Hello hello = new Hello();
          hello.setName(name);
          return hello;
      }
      static class Hello {
          private String name;
          // Getter and Setter 방식 - 프로퍼티 접근 방식 = 자바빈
          public String getName() {
              return name;
        }
          public void setName(String name) {
              this.name = name;
        } 
    }
}
```
`http://localhost:8080/hello-api?name=서윤`  
  
<img src ="https://velog.velcdn.com/images/khoony0125/post/6d327242-5cb4-428d-9e7d-e05d4a5df525/image.png">  

- `@GetMapping("hello-api")`를 컨트롤러에서 찾아봐.
- 어? `@ResponseBody`가 붙어있네. Http의 BODY로 직접 반환해야지.
- 객체면 Json으로, 문자열이면 String으로 변환해야 겠다.
- 객체니까 JSON스타일로 변환해서 웹 브라우저에 보내주자.
