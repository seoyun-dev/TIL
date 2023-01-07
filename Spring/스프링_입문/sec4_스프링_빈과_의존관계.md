# 스프링 빈과 의존 관계(한 번 다시 듣는 것 추천)
## 컴포넌트 스캔과 자동 의존관계 설정
멤버 Controller가 멤버 서비스를 통해 회원가입하고 데이터를 조회할 수 있어야한다.(멤버 controller가 멤버 service를 의존한다.) 그리고 template을 이용하여 html에 뿌려준다.  
- 생성자에 @Autowired 가 있으면 스프링이 연관된 객체를 스프링 컨테이너에서 찾아서 넣어준다. 이렇게 객체 의존관계를 외부에서 넣어주는 것을 DI (Dependency Injection), 의존성 주입이라 한다.
- 이전 테스트에서는 개발자가 직접 주입했고, 여기서는 @Autowired에 의해 스프링이 주입해준다  

> memberController 생성 → 스프링 컨테이너에서 @Controller 확인 후 스프링 컨테이너에 등록하면서 생성자 호출 → 이 때 @AutoWired 확인해서 memberController 가 memberService 를 필요로 한다는 사실 확인하여 컨테이너에 있는 memberService 를 넣어준다.  
여기서 service 와 repository 간에도 같은 과정 반복. 단지 memberRepository 가 아니라 구현체인 memoryMemberRepository 가 대상이다.

- @Component 어노테이션이 있으면 스프링 빈으로 자동 등록된다.
- @Controller 컨트롤러가 스프링 빈으로 자동 등록된 이유도 컴포넌트 스캔 때문이다.  
- @Component 를 포함하는 다음 어노테이션도 스프링 빈으로 자동 등록된다.
  - @Controller
  - @Service
  - @Repository  
- 스프링 빈 등록은 @Component , 연결은 @AutoWired !

## 자바 코드로 직접 스프링 빈 등록하기
ServiceConfig
service 패키지 아래 ServiceConfig 파일을 생성하여 다음과 같이 작성한다.
```java
package hello.hellospring.service;

import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
}
```
DI에는 필드 주입, setter 주입, 생성자 주입 이렇게 3가지 방법이 있다. 의존관계가 실행중에
동적으로 변하는 경우는 거의 없으므로 생성자 주입을 권장한다.