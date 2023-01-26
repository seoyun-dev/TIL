package Java.src.Q_6_20;

public class Account {
    private int[] balance = 0;
    String[] accountNumber;
    String[] master;

    public void addAccount(int amount) {
        this.balance += amount;
    }
    public void minusAccount(int amount) {
        this.balance -= amount;
    }
}
