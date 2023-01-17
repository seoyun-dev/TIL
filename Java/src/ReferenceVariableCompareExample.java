package Java.src;

public class ReferenceVariableCompareExample {
    public static void main(String[] args) {
        int[] arr1 = {1, 3, 3};
        int[] arr2 = {1, 3, 3};
        int[] arr3;
    
        //배열 {1, 2, 3}을 힙에 생성하고 arr1에 번지 대입
        // arr1 = new int[] {1, 2, 3}; 
        //배열 {1, 2, 3}을 힙에 생성하고 arr2에 번지 대입
        // arr2 = new int[] {1, 2, 3};
        //arr2 값(배열 번지)를 arr3 에 대입
        arr3 = arr2;
        String c = "가";
        String d = new String("가");
        System.out.println(c == d);
        System.out.println(arr1 == arr2); //서로 다른 배열 객체 -> false
        System.out.println(arr1 != arr2); //서로 같은 배열 객체 -> true
    }
}