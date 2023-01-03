package Java.이것이_자바다.src;

public class TextBlockExample {
    public static void main (String[] args) {
        String str1 = """
                {
                    "id": "winter",
                    "name": "눈송이"
                }
                """;
        String str2 = """
                나는 자바를 \
                학습합니다.
                나는 자바 고수가 될 겁니다.
                """;  // 줄바꿈 하지 않고 다음 줄에 이어서 작성하고 싶을 때 맨 끝에 \
                System.out.println("str1: "+ str1);
        System.out.println("str2: "+ str2);
    }
}