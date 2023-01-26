package Java.src.Q_6_19;

public class Account {
    private int balance;
    public static final int MIN_BALANCE = 0;
    public static final int MAX_BALANCE = 1000000;

    public void setBalance(int balance) {
        if(0 <=balance && balance <= 1000000) {
            this.balance = balance;
        }
    }

    public int getBalance() {
        return balance;
    }
}