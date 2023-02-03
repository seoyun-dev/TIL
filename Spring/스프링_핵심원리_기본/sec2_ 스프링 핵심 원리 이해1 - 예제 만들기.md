# 스프링 핵심 원리 이해1 - 예제 만들기  


## 프로젝트 생성
이번엔 스프링도 쓰지 않고 순수하게 자바만 사용할 것이다.  
스프링 코어가 있는 이유는 뒤에서 스프링을 사용할 것이기 때문이다.  

- 프로젝트 선택
  - Project: Gradle - Groovy Project Spring Boot: 2.3.x
  - Language: Java
  - Packaging: Jar
  - Java: 11 
- Project Metadata
  - groupId: hello
  - artifactId: core 
- Dependencies: 선택하지 않는다.  

아무것도 하지 않은 상태에서 RUN 가능 -> 스프링 웹 프로젝트를 넣은게 아니므로 실행만 되고 끝나는게 맞음  
- Preferences Build, Execution, Deployment Build Tools Gradle 
  - Build and run using: Gradle IntelliJ IDEA
  - Run tests using: Gradle IntelliJ IDEA
## 비즈니스 요구사항과 설계
- 회원
  - 회원을 가입하고 조회할 수 있다.
  - 회원은 일반과 VIP 두 가지 등급이 있다.
  - 회원 데이터는 자체 DB를 구축할 수 있고, 외부 시스템과 연동할 수 있다. (미확정)
- 주문과 할인 정책
  - 회원은 상품을 주문할 수 있다.
  - 회원 등급에 따라 할인 정책을 적용할 수 있다.
  - 할인 정책은 모든 VIP는 1000원을 할인해주는 고정 금액 할인을 적용해달라. (나중에 변경 될 수 있다.)
  - 할인 정책은 변경 가능성이 높다. 회사의 기본 할인 정책을 아직 정하지 못했고, 오픈 직전까지 고민을 미루고 싶다. 최악의 경우 할인을 적용하지 않을 수 도 있다. (미확정)

요구사항을 보면 회원 데이터, 할인 정책 같은 부분은 지금 결정하기 어려운 부분이다. 그렇다고 이런 정책이 결정될 때 까지 개발을 무기한 기다릴 수 도 없다. 우리는 앞에서 배운 객체 지향 설계 방법이 있지 않은가!  

인터페이스를 만들고 구현체를 언제든지 갈아끼울 수 있도록 설계하면 된다. 그럼 시작해보자.  

> 참고: 프로젝트 환경설정을 편리하게 하려고 스프링 부트를 사용한 것이다. 지금은 스프링 없는 순수한 자바로만 개발을 진행한다는 점을 꼭 기억하자! 스프링 관련은 한참 뒤에 등장한다.
## 회원 도메인 설계
- 회원 도메인 요구사항
  - 회원을 가입하고 조회할 수 있다.
  - 회원은 일반과 VIP 두 가지 등급이 있다.
  - 회원 데이터는 자체 DB를 구축할 수 있고, 외부 시스템과 연동할 수 있다. (미확정) → 인터페이스와 클래스로 → 개발용으론 간단한 메모리 회원 저장소로 우선 사용(재부팅시 데이터가 날라가므로 DB 확정 전까지의 개발용)

![](https://user-images.githubusercontent.com/91110192/215238613-dc6b4134-e12c-4700-adcd-6d613e46c645.png)  

> repository v.s. service  
repository 패키지는 DB에 접근하는 모든 코드가 모여있다고 생각하시면 됩니다.  
service 패키지는 DB에 접근하는 코드는 repository에 위임하고, 비즈니스 로직과 관련된 모든 코드가 모여있습니다.  
이렇게 구분해두면 비즈니스 로직과 관련된 부분에 문제가 발생했을 때는 service 패키지를 확인하고, DB 접근과 관련된 문제가 발생하면 repository 부분을 확인하면 되겠지요^^?


## 회원 도메인 개발
### 회원 엔티티
- 회원 등급 : `src/main/java/hello.core/member/Grade`
- 회원 엔티티 : `src/main/java/hello.core/member/Member`

### 회원 저장소
- 회원 저장소 인터페이스 : `src/main/java/hello.core/member/MemberRepository`
- 메모리 회원 저장소 구현체 : `src/main/java/hello.core/member/MemoryMemberRepository`

### 회원 서비스
- 회원 서비스 인터페이스 : `src/main/java/hello.core/member/MemberService`
- 회원 서비스 구현체 : `src/main/java/hello.core/member/MemberServiceImpl`

## 회원 도메인 실행과 테스트
- 회원 도메인 - 회원 가입 테스트 : `src/test/hello.cor/member/memberServiceTest`  

**회원 도메인 설계의 문제점**
- 이 코드의 설계상 문제점은 무엇일까요?
- 다른 저장소로 변경할 때 OCP 원칙을 잘 준수할까요?
- DIP를 잘 지키고 있을까요?
- 의존관계가 인터페이스 뿐만 아니라 구현까지 모두 의존하는 문제점이 있음(DIP 위반)
  - -> 주문까지 만들고나서 문제점과 해결 방안을 설명  
  ```java
  public class MemberServiceImpl implements MemberService {
    //DIP 위반
    //MemberServiceImpl은 MemberRepository(인터페이스) 뿐만 아니라 MemoryMemberRepository(구현체)에도 의존
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    ...
  }
  ```
## 주문과 할인 도메인 설계
- 주문과 할인 정책
  - 회원은 상품을 주문할 수 있다.
  - 회원 등급에 따라 할인 정책을 적용할 수 있다.
  - 할인 정책은 모든 VIP는 1000원을 할인해주는 고정 금액 할인을 적용해달라. (나중에 변경 될 수 있다.)
  - 할인 정책은 변경 가능성이 높다. 회사의 기본 할인 정책을 아직 정하지 못했고, 오픈 직전까지 고민을 미루고 싶다. 최악의 경우 할인을 적용하지 않을 수 도 있다. (미확정)  

**주문 도메인 협력, 역할, 책임**  

![](https://user-images.githubusercontent.com/91110192/216542692-27206351-c9d6-4b71-a8ac-e381c81aa065.png)

> 역할만 구현  

1. 주문 생성: 클라이언트는 주문 서비스에 주문 생성을 요청한다.
2. 회원 조회: 할인을 위해서는 회원 등급이 필요하다. 그래서 주문 서비스는 회원 저장소에서 회원을 조회한다.
3. 할인 적용: 주문 서비스는 회원 등급에 따른 할인 여부를 할인 정책에 위임한다. 
4. 주문 결과 반환: 주문 서비스는 할인 결과를 포함한 주문 결과를 반환한다.
> 참고: 실제로는 주문 데이터를 DB에 저장하겠지만, 예제가 너무 복잡해 질 수 있어서 생략하고, 단순히 주문 결과를 반환한다.

**주문 도메인 전체**  

![](https://user-images.githubusercontent.com/91110192/216542685-ed4adfa7-16c7-4561-b1db-2594af553f1f.png)  

> 역할과 구현 모두  

**역할과 구현을 분리**해서 자유롭게 구현 객체를 조립할 수 있게 설계했다. 덕분에 회원 저장소는 물론이고, 할인 정책도 유연하게 변경할 수 있다.


**주문 도메인 클래스 다이어그램**
![](https://user-images.githubusercontent.com/91110192/216542664-8076171f-0437-410c-a103-22ac0d9d69ac.png)

**주문 도메인 객체 다이어그램1**  
![](https://user-images.githubusercontent.com/91110192/216542681-39fcbcea-76ff-4692-a1c2-818ecbe07ab2.png)  

회원 저장소 구현체 또는 할인 정책의 구현체가 바뀌어도 주문 서비스를 변경하지 않아도 된다. 즉, 역할들의 협력 관계를 그대로 재사용 할 수 있다.

**주문 도메인 객체 다이어그램2**  

![](https://user-images.githubusercontent.com/91110192/216542676-a0045841-a1ed-454b-a7ed-bb2ef1062081.png)  

회원을 메모리가 아닌 실제 DB에서 조회하고, 정률 할인 정책(주문 금액에 따라 % 할인)을 지원해도 주문 서비스를 변경하지 않아도 된다.
협력 관계를 그대로 재사용 할 수 있다.

## 주문과 할인 도메인 개발
- 주문 서비스
  - 주문 엔티티 : `src/main/java/hello.core/order/Order`
  - 주문 서비스 인터페이스: `src/main/java/hello.core/order/OrderService`
  - 주문 서비스 구현체 : `src/main/java/hello.core/order/OrderServiceImpl`
- 할인 정책
  - 할인 정책 인터페이스 : `src/main/java/hello.core/discount/DiscountPolicy`
  - 정액 할인 정책 구현체 : `src/main/java/hello.core/discount/FixDiscountPolicy`

## 주문과 할인 도메인 실행과 테스트