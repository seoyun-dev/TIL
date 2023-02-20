# 스프링 컨테이너와 스프링 빈
> 추가 설명만 작성 시작.?


지금까지는 왜 스프링이 만들어졌는지 설명했다면, 이제부터는 진짜 스프링에 대해 설명할 것이다.  

## 스프링 컨테이너 생성
- `AnnotationConfigApplicationContext`는 `ApplicationContext` 인터페이스(스프링 컨테이너)의 구현체이다.  
- 컨테이너는 객체를 담아두는 곳이라고 볼 수 있다.

## 컨테이너에 등록된 모든 빈 조회
appConfig도 빈으로 등록된다.  

## 스프링 빈 조회 - 기본
```java
public class ApplicationContextBasicFindBean {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("빈 이름으로 조회")

    void findBeanByName() {
        //memberService()로부터 반환된 실제 객체(MemberServiceImpl 타입)를
        //MemberService 타입의 변수인 memberService 로 받음.
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        //따라서, memberService.isInstanceOf(MemberServiceImpl.class)를 실행하면
        //memberService 변수 내에 담긴 실제 객체(MemberServiceImpl타입의 객체)가 MemberServiceImpl 타입의 인스턴스인지 비교하게 됨.
        Assertions.assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }
}
```
## 스프링 빈 조회 - 동일한 타입이 둘 이상

## 스프링 빈 조회 - 상속 관계
부모 타입을 조회하면 자식 타입들은 다 끌려나온다!   
Java의 최고 부모는 Object(class의 최고 부모도 Object)

```java
@Configuration
    static class TestConfig {
        @Bean
        //DiscountPolicy 대신 RateDiscountPolicy를 해도 된다
        //하지만 구현보단 역할인 DiscountPolicy를 사용하는 것이 좋음
        public DiscountPolicy rateDiscountPolicy() {
            return new RateDiscountPolicy();
        }
    }
```
## Bean Factory와 Application Context
ApplicatonContext가 제공하는 부가기능은 다른 강의에서 자세히 알아보도록 하겠다.

## 다양한 설정 형식 지원 - 자바 코드, XML
지금까지는 자바코드로 설정하는 방법을 알아보았는데, 이번에는 XML로 설정하는 방법을 간단히 알아보겠다.

요즘은 자바코드 기반의 설정파일(AppConfig.class)을 많이 설정한다. 예전엔 xml로(appConfig.xml) 많이 사용했으므로, 어떻게 돌아가는지는 알아두자.
## 스프링 빈 설정 메타 정보 - BeanDefinition
스프링에 빈 등록하는 방법 크게 두가지

1. 직접 스프링 빈 등록 - AppConfig.xml
2. 팩토리 메서드 사용(우회) - appConfig.class  
factory bean(팩토리 메서드)을 통해 등록하는 방식  

>생성자 대신 오브젝트를 생성해주는 코드의 도움을 받아서 빈 오브젝트를 생성하는 것을 팩토리 빈이라고 함