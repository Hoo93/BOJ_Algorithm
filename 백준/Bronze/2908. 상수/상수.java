import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String input1 = st.nextToken();
        String input2 = st.nextToken();

        int num1 = Integer.parseInt(new StringBuilder(input1).reverse().toString());
        int num2 = Integer.parseInt(new StringBuilder(input2).reverse().toString());

        System.out.println(Math.max(num1, num2));
    }
}


