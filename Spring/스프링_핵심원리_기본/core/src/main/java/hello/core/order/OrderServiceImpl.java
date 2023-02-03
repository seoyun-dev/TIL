package hello.core.order;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.FixDiscountPolicy;
import hello.core.member.Member;
import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;

public class OrderServiceImpl implements OrderService {

    //회원조회와 할인적용을 위해
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    private final DiscountPolicy discountPolicy = new FixDiscountPolicy();

    @Override
    public Order createOrder(Long memberId, String itemName, int itemprice) {
        Member member = memberRepository.findById(memberId);
        //할인관련해서는 아는게 없다! discountPolicy 에 던져주고 결과만 받음 -> 단일책임원칙 굿
        int discountPrice = discountPolicy.discount(member, itemprice);

        return new Order(memberId, itemName, itemprice, discountPrice);
    }
}
