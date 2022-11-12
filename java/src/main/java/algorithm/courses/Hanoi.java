package algorithm.courses;


public class Hanoi {
    public void sort1(int n) {
        if (n > 0) {
            func(n, "left", "right", "mid");
        }


    }

    private void func(int n, String from, String to, String other) {
        if (n == 1) {
            System.out.println("Move 1 from " + from + " to " + to);
        } else {
            func(n - 1, from, other, to);
            System.out.println("Move " + n + " from " + from + " to " + to);
            func(n - 1, other, to, from);
        }
    }
    
}
