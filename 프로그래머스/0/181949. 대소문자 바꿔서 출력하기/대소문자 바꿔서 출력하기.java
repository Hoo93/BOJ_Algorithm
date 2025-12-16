import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        StringBuilder sb = new StringBuilder();
        
        for (char i : a.toCharArray()) {
            // Upper Case
            if (i - 'a' < 0) sb.append((char) (i + 32));
            // Lower Case
            else sb.append((char) (i - 32));
        }
        
        System.out.printf(sb.toString());
    }
}