package Java.src;

public class BreakOutterExample {
    public static void main(String[] args) {
        Outter: for(char i='A'; i<='C'; i++) {
            Inner: for(char j='a'; j<='c'; j++) {
                last: for(int k=1; k<=3; k++) {
                    System.out.println("k:" + k);
                    if(k==2) {
                        break Inner;
                    }
                }
                System.out.println("j:" + j);
            }
            System.out.println("i:" + i);
        }
    }
}
