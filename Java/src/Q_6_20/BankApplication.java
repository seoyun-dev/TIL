package Java.src.Q_6_20;

import java.util.Scanner;
import Java.src.Q_6_20.Account;

public class BankApplication {
    public static void main(String[] args){
        boolean run = true;
        Scanner scanner = new Scanner(System.in);
        Account account = new Account();

        while(run) {
            System.out.println("--------------------------------------");
            System.out.println("1.계죄생성|2.계좌목록|3.예금|4.출금|5.종료");
            System.out.println("--------------------------------------");
            System.out.print("선택> ");
            String choice = scanner.nextLine();
            switch(choice) {
                case "1" -> {
                    System.out.println("--------------");
                    System.out.println("계좌생성");
                    System.out.print("계좌번호: ");
                    account.accountNumber = scanner.nextLine();
                    System.out.println("--------------");
                    System.out.println("--------------");
                    System.out.println("--------------");
                    System.out.println("--------------");
                }
            }
            
        }
    }
}
