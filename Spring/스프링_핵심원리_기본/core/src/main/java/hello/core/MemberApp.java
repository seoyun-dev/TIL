package hello.core;

import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

//Test 대용. Test로 하는 것이 더 중요
public class MemberApp {
    //아래는 순수한 자바코드 (스프링 x) -> Junit 프레임워크 사용해보자
    public static void main(String[] args) {
//        AppConfig appConfig = new AppConfig();
//        MemberService memberService = appConfig.memberService();

        //ApplicationContext가 스프링 컨테이너라고 보면 된다
        //AppConfig에 있는 설정 정보를 가지고 반환된 객체를 스프링 컨테이너에 저장
        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        //빈 찾는 방법: getBean(이름, 타입)
        MemberService memberService = applicationContext.getBean("memberService", MemberService.class);


        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        Member findMember = memberService.findMember(1L);
        System.out.println("new member = " + member.getName());
        System.out.println("findMember = " + findMember.getName());
    }
}
