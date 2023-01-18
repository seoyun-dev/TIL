package Java.src;

public class Test {
    public static void main(String[] args) {
        if(args.length != 2) {    //입력된 데이터 개수가 2개가 안되면
            System.out.println("프로그램 입력값 부족");
            System.exit(0);       //프로그램 강제 종료
        }
        String strNum1 = args[0]; //데이터 얻기
        String strNum2 = args[1];
    
        int num1 = Integer.parseInt(strNum1);
        int num2 = Integer.parseInt(strNum2);
    
        int result = num1 + num2;
        System.out.println(num1 + " + " + num2 + " + " + result);
    }
}