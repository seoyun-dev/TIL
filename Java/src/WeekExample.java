package Java.src;

import java.util.Calendar;

public class WeekExample {
    public static void main(String[] args) {
        //열거 타입도 데이터 타입이므로 변수를 선언하고 사용
        //열거 타입도 참조 타입이므로 null 대입 가능
        Week today = null;

        //Calendar 객체를 얻고 번지를 cal 변수에 대입
        Calendar cal = Calendar.getInstance();

        //일(1)~토(7)까지의 숫자를 얻고 week 변수에 대입
        int week = cal.get(Calendar.DAY_OF_WEEK);

        //숫자를 열거 상수로 변환해서 변수에 대입
        switch(week) {
            //열거 상수 대입시 '열거타입.열거상수' 형태로 작성
            case 1: today = Week.SUNDAY; break;
            case 2: today = Week.MONDAY; break;
            case 3: today = Week.TUESDAY; break;
            case 4: today = Week.WEDNESDAY; break;
            case 5: today = Week.THURSDAY; break;
            case 6: today = Week.FRIDAY; break;
            case 7: today = Week.SATURDAY; break;
        }
    
        //열거 타입 변수를 사용
        if(today == Week.SUNDAY) {
            System.out.println("일요일엔 놀자");
        } else {
            System.out.println("자바 공부하자");
        }
    }
}
