package Java.src;

public class KoreanExample {
    public static void main(String[] args) {
        Korean k1 = new Korean("123456-1234567", "박서윤");

        System.out.println(k1.nation);
        System.out.println(k1.ssn);
        System.out.println(k1.name);
        
        k1.name = "박해피";

        System.out.println("k1.name");
    }
}
