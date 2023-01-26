package Java.src;

import Java.src.Q_6_19.Account;

public class Test {
    public static void main(String[] args) {
        Account account = new Account();

        account.setBalance(1000);
        System.out.println(account.getBalance());
        account.setBalance(-100);
        System.out.println(account.getBalance());
        account.setBalance(2000000);
        System.out.println(account.getBalance());
        account.setBalance(30000);
        System.out.println(account.getBalance());
    }
}