package Java.src;
import java.util.Scanner;

public class DoWhileExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputString;

        System.out.println("메시지 입력하세요.");
        System.out.println("프로그램을 종료하려면 q를 입력하세요.");

        do{
            System.out.print(">");
            inputString = scanner.nextLine();
            System.out.println(inputString);
        } while(!inputString.equals("q"));
        
        System.out.println();
        System.out.println("프로그램 종료");
    }
}
