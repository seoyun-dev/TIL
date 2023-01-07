# 회원 관리 예제 - 백엔드 개발    
## 비즈니스 요구사항 정리  
- 데이터: 회원ID, 이름
- 기능: 회원 등록, 조회  
- 아직 데이터가 선정되지 않음(가상의 시나리오)  
  

![](https://user-images.githubusercontent.com/91110192/210940737-88380348-ade7-41de-b6d8-0ee4d060ccdb.png)  
- 컨트롤러: 웹 MVC의 컨트롤러 역할. Mapping으로 주소 찾아 정보를 Service에 전달.
- 서비스: 핵심 비즈니스 로직 구현, 예) 회원 중복가입 불가
- 리포지토리: 데이터베이스에 접근, 도메인 객체를 DB에 저장하고 관리
- 도메인: 비즈니스 도메인 객체, 예) 회원, 주문, 쿠폰 등등 주로 데이터베이스에 저장하고 관리됨  

![](https://user-images.githubusercontent.com/91110192/210940734-c9d02f84-a7c7-4e67-b6fc-dd656f74881b.png)  
- 데이터 저장소가 선정되지 않아, 우선 인터페이스로 구현 클래스를 변경할 수 있도록 설계

## 회원 도메인과 리포지토리 만들기  
추후 코드 정리하여 연관짓기

## 회원 리포지토리 테스트 케이스 작성
자바는 JUnit이라는 프레임워크로 테스트를 주로 실행한다.  
테스트는 순서보장이 되어있지 않으므로 순서에 의해 설계하지 않아야 한다. 그러다보니 한번에 여러 테스트를 실행시 메모리 DB에 직전 테스트의 결과가 남아 테스트를 실패할 가능성이 있다.  
이 때, `@AfterEach`를 사용하면 각 테스트가 종료될 때마다 이 기능을 실행한다. 여기서는 메모리 DB에 저장된 데이터를 삭제한다.  

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.ClassBasedNavigableIterableAssert.assertThat;

//굳이 public 안해도 됨
class MemoryMemberRepositoryTest {
    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }
    @Test
    public void save() {
        Member member = new Member();
        member.setName("spring");

        repository.save(member);

        //Optional에서 꺼낼 때 get() 쓸 수 있음. 좋은 방법은 아니지만 테스트 코드에선 사용하지 뭐
        Member result = repository.findById(member.getId()).get();
        Assertions.assertThat(member).isEqualTo(result);
    }

    @Test
    public void findByName() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        Member result = repository.findByName("spring1").get();
        Assertions.assertThat(result).isEqualTo(member1);
    }

    @Test
    public void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();
        Assertions.assertThat(result.size()).isEqualTo(2);
    }
}
```

## 회원 서비스 개발
_src에 기록__  



## 회원 서비스 테스트

회원 리포지토리의 코드가
회원 서비스 코드를 DI(Dependency Injection) 가능하게 변경한다.  
```Java
//MemberService
  public class MemberService {
      private final MemberRepository memberRepository;
      public MemberService(MemberRepository memberRepository) {
          this.memberRepository = memberRepository;
}
... }
```
```java
MemberService memberService;
MemoryMemberRepository memberRepository;

// 테스트 실행 전 호출
@BeforeEach
public void beforeEach() {
    memberRepository = new MemoryMemberRepository();
    memberService = new MemberService(memberRepository);
}
```