import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = Integer.parseInt(sc.nextLine());

        while (T-- > 0) {
            String input = sc.nextLine();

            Deque<Character> left = new ArrayDeque<>();
            Deque<Character> right = new ArrayDeque<>();

            for (char ch : input.toCharArray()) {
                if (ch == '<') {
                    if (!left.isEmpty()) right.push(left.pop());
                } else if (ch == '>') {
                    if (!right.isEmpty()) left.push(right.pop());
                } else if (ch == '-') {
                    if (!left.isEmpty()) left.pop();
                } else {
                    left.push(ch);
                }
            }

            StringBuilder sb = new StringBuilder();
            while (!left.isEmpty()) sb.append(left.removeLast());
            while (!right.isEmpty()) sb.append(right.removeFirst());
            System.out.println(sb);
        }
    }
}