# 프로젝트 환경설정
## 프로젝트 생성
start.spring.io 는 spring boot를 기반으로 spring 관련 프로젝트를 만들어주는 사이트
- Project: Gradle-Groovy
- Language: Java
- Packaging: Jar
- group(회사명, 그룹명), artifact(프로젝트명)
- Dependencies: Spring Web, Thymelear
</br>
</br>

## 라이브러리 살펴보기
> Gradle은 의존관계가 있는 라이브러리르 함께 다운한다.  

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
  - mockito: 목 라이브러리
  - assertj: 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리 
  - spring-test: 스프링 통합 테스트 지원
</br>
</br>
  
## View 환경설정  

> Spring은 어마어마하게 크기 때문에 머리에 다 담을 수 X.  
즉, 필요한 것을 찾는 능력이 중요!   
spring.io에 접속 -> [project] - [spring boot] - [Reference Doc] 들어가서 검색해 찾기    

<img src="https://images.velog.io/images/hono2030/post/76309860-e16d-46c7-ade9-0d2790e58abe/image.png">
  
- 톰캣: hello가 들어왔네? 컨트롤러 중에 mapping("hello") 찾아!
- 찾았다! return: hello 니까 뷰리졸버로 템플릿 엔진에서 hello.html 찾아.
    - `resources:templates/` +{ViewName}+ `.html`
- html 템플릿 웹브라우저에 보내자.

</br>
</br>

## 빌드하고 실행하기
cmd창에서 실행 ( InteliJ에서 실행하는 것과 동일 )
1. `./gradlew build`
2. `cd build/libs`
3. `java -jar hello-spring-0.0.1-SNAPSHOT.jar`
4. 실행 확인