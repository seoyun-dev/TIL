package hello.core.beanfind;

import hello.core.AppConfig;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

public class ApplicationContextBasicFindBean {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("빈 이름으로 조회")
    void findBeanByName() {
        //memberService()로부터 반환된 실제 객체(MemberServiceImpl 타입)를
        //MemberService 타입의 변수인 memberService 로 받음.
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        //따라서, memberService.isInstanceOf(MemberServiceImpl.class)를 실행하면
        //memberService 변수 내에 담긴 실제 객체(MemberServiceImpl 타입의 객체)가 MemberServiceImpl 타입의 인스턴스인지 비교하게 됨.
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("이름 없이 타입으로만 조회")
    void findBeanByType() {
        MemberService memberService = ac.getBean(MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    //가능하지만 좋지 않다. 역할과 구현을 구분해야 하고, 역할에 의존해야 하기 때문.
    @Test
    @DisplayName("구체 타입으로 조회")
    void findBeanByType2() {
        MemberService memberService = ac.getBean("memberService", MemberServiceImpl.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("빈 이름으로 조회 X")
    void findByNameX() {
        //ac.getBean(..)을 실행하면 NoSuchBeanDefinitionException 예외가 터져야 성공
        assertThrows(NoSuchBeanDefinitionException.class,
                () -> ac.getBean("xxxxx", MemberService.class));
    }
}
