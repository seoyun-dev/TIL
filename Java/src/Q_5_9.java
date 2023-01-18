package Java.src;

import java.util.Scanner;

public class Q_5_9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean run = true;
        int[] scores = null; 
            
        while(run) {
            System.out.println("-------------------------------------------------------");
            System.out.println("1.학생수 | 2.점수입력 | 3.점수리스트 | 4.분석 | 5.종료");
            System.out.println("-------------------------------------------------------");
            System.out.print("선택> ");
            int choice = scanner.nextInt();

            switch(choice) {
                case 1 -> {
                    System.out.print("학생수> ");
                    scores = new int[scanner.nextInt()];
                }
                case 2 -> {
                    for(int j=0; j<scores.length; j++) {
                        System.out.print("scores[" + j + "]> ");
                        scores[j] = scanner.nextInt();
                    }
                }
                case 3 -> {
                    for(int j=0; j<scores.length; j++) {
                        System.out.println("scores[" + j + "]: " + scores[j]);
                    }
                }
                case 4 -> {
                    int sum = 0;
                    int max = 0;
                    for(int j=0; j<scores.length; j++) {
                        if(max < scores[j]) {
                            max = scores[j];
                        }
                        sum += scores[j];
                    }
                    double avg = (double)sum / scores.length;
                    System.out.println("최고 점수: " + max);
                    System.out.println("평균 점수: " + avg);
                }
                case 5 -> {
                    run = false;
                }
            }
        }
    }
}