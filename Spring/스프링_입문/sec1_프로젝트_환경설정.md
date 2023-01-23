# 프로젝트 환경설정
대부분의 개발자들이 스프링을 포기하는 이유는 처음부터 IOC, DI, AOP 같은 이론적 내용부터 학습하기 때문이다.  
스프링은 웹 애플리케이션을 개발하기 위해 존재한다.  
그러므로 우리는 '간단한 웹 애플리케이션 개발'을 하기 위해 아래 단계를 빠르게 수행하며 스프링을 배울 것이다.
- 스프링 프로젝트 생성
- 스프링 부트로 웹 서버 실행
- 회원 도메인 개발
- 웹 MVC 개발
- DB 연동 - JDBC, JPA, 스프링 데이터 JPA
- 테스트 케이스 작성  

프로젝트에서 사용하는 최신 기술들로는 Spring Boot, Gradle, Thymeleaf, JPA, HIBERNATE, Tomcat이 있다.
이 사용기술들이 어떻게 사용되는지 전반적인 감을 잡고 큰 그림을 잡는 것이 이 강의의 목표이다.  

**강의 핵심 목표**  
스프링 학습의 제대로 된 첫 길잡이 역할
- 스프링 기술 그 자체에 매몰 X
- 어떻게 사용하는지에 초점
- 오래되거나 마이너한 스프링 기술 과감히 X
- 실무 개발에 꼭 필요한 내용의 스프링 학습

## 프로젝트 생성
start.spring.io 는 spring boot를 기반으로 spring 관련 프로젝트를 만들어주는 사이트
- Project: Gradle-Groovy(gradle은 버전 설정과 라이브러리 당겨오는 역할을 해줌)
- Language: Java
- Spring Boot: SNAPSHOT(테스트버전), M1 제외한 가장 최신 버전 선택 
- Packaging: Jar
- group(기업 도메인명/hello), artifact(프로젝트명/hello-spring)
- Dependencies: Spring Web, Thymelear
</br>

![](https://user-images.githubusercontent.com/91110192/214016262-874c901f-f3af-4b11-a295-cd273601cf5d.png)  
- .gradle, .idea 무시
- gradle: gradle 관련
- src  
  - main
    - java: java code
    - resources: java 코드 파일 제외한 XML, 설정파일, HTML 등 모든 것
  - test: test code
- .gitignore: 
- build.gradle: gradle 설정  

## 라이브러리 살펴보기 - 편하게 듣자..! 그냥 들으며 감 잡기
> Gradle은 의존관계가 있는 라이브러리르 함께 다운한다.  

![](https://user-images.githubusercontent.com/91110192/214021059-a3ecdbcf-cf83-4eb1-9fdf-249250b62986.png)  

위처럼 starter web 라이브러리를 받으면 아래의 의존관계에 있는 모든 라이브러리를 다운받게 된다.


**스프링 부트 라이브러리**
- spring-boot-starter-web
  - spring-boot-starter-tomcat: 톰캣 (웹서버) 
  - spring-webmvc: 스프링 웹 MVC
- spring-boot-starter-thymeleaf: 타임리프 템플릿 엔진(View) 
- spring-boot-starter (공통): 스프링 부트 + 스프링 코어 + 로깅
  - spring-boot 
    - spring-core
  - spring-boot-starter-logging 
    - logback, slf4j  

**테스트 라이브러리**
- spring-boot-starter-test
  - junit: 테스트 프레임워크
  - mockito: 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리 
  - assertj: 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리 
  - spring-test: 스프링 통합 테스트 지원
</br>
</br>
  
## View 환경설정  

> Spring은 어마어마하게 크기 때문에 머리에 다 담을 수 X.  
즉, 필요한 것을 찾는 능력이 중요!   
spring.io에 접속 -> [project] - [spring boot] - [Reference Doc] 들어가서 검색해 찾기    

<img src="https://images.velog.io/images/hono2030/post/76309860-e16d-46c7-ade9-0d2790e58abe/image.png">
  
- 톰켓서버: hello가 들어왔네? 스프링아, 컨트롤러 중에 mapping("hello") 찾아!
- 스프링: 찾았다! `@GetMapping("hello")`된 부분 내가 모델 만들어서 넣어가지구 실행해야지! `return "hello";` 니까 뷰리졸버로 템플릿 엔진에서 hello.html 찾아.
    - `resources:templates/` +{ViewName}+ `.html`
- hello.html 템플릿 웹브라우저에 보내자.

</br>
</br>

## 빌드하고 실행하기
cmd창에서 실행 ( InteliJ에서 실행하는 것과 동일. 같은 8080 포트를 사용하므로 둘 중 하나만 실행하면 됨. )
1. `./gradlew build`
2. `cd build/libs`
3. `java -jar hello-spring-0.0.1-SNAPSHOT.jar`
4. 실행 확인

서버 배포할때는 `hello-spring-0.0.1-SNAPSHOT.jar` 파일만 복사하여 서버에 넣어주고, 실행시키면 된다.