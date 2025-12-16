import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        StringBuilder sb = new StringBuilder();
        int difference = 'a' - 'A';
        
        for (char i : a.toCharArray()) {
            // Lower Case
            if (i >= 'a') sb.append((char) (i - difference));
            // Uppser Case
            else sb.append((char) (i + difference));
        }
        
        System.out.printf(sb.toString());
    }
}