public class Driver {
    static int fib(int n) {
        if(n < 2) {
            return n;
        }
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        System.out.println(fib(20));
        long endTime = System.currentTimeMillis();
        long elapsedTime = endTime - startTime;
        System.out.println(elapsedTime);
    }
}
