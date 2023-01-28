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


## 회원 도메인 개발
### 회원 엔티티
- 회원 등급 : src/main/java/hello.core/member/Grade
- 회원 엔티티 : src/main/java/hello.core/member/Member

### 회원 저장소
- 회원 저장소 인터페이스 : src/main/java/hello.core/member/MemberRepository
- 메모리 회원 저장소 구현체 : src/main/java/hello.core/member/MemoryMemberRepository

### 회원 서비스
- 회원 서비스 인터페이스 : src/main/java/hello.core/member/MemberService
- 회원 서비스 구현체 : src/main/java/hello.core/member/MemberServiceImpl

## 회원 도메인 실행과 테스트

## 주문과 할인 도메인 설계

## 주문과 할인 도메인 개발

## 주문과 할인 도메인 실행과 테스트