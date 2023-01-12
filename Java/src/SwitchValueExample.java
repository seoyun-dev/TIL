package Java.src;

public class SwitchValueExample {
    public static void main(String[] args) {
        String grade = "B";
        
        //Java 11 이전 문법
        int score1 = switch(grade) {
            case "A" -> 100;
            case "B" -> {
                int result = 100 - 20;
                yield result;
            }
            default -> 60;
        };
        System.out.println("score1: " + score1);
    }
}