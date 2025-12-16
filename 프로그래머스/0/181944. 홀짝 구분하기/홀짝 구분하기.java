import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        boolean isEven = n % 2 == 0;
        
        System.out.print(n + " is " + (isEven ? "even" : "odd"));
    }
}