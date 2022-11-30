import java.math.BigInteger;
import java.util.*;

class shors {
    public static BigInteger find_gcd(BigInteger number_1, BigInteger number_2) {
        return number_1.gcd(number_2);
    }

    public static int get_random_number(int lower_bound, int upper_bound){
        return (int) ((Math.random() * (upper_bound - lower_bound)) + lower_bound);
    }

    public static void shors_algorithm(int number_to_factor){
        int N = number_to_factor;
        int K = get_random_number(1, number_to_factor);
        BigInteger gcd = find_gcd(BigInteger.valueOf(N), BigInteger.valueOf(K));
        int GCD = gcd.intValue();
        if (GCD != 1)
            System.out.println(GCD + " is a factor of " + N);
        else{
            List<Integer> transformations = new ArrayList();
            int q = 1;
            int iterations = 0;
            while (true){
                q = (q*K) % N;
                transformations.add(q);
                iterations++;
                if (q == 1)
                    break;
            }
            if (iterations % 2 != 0){
                System.out.println("Number of iterations is not even");
                shors_algorithm(N);
            }
            else{
                int p = transformations.get(((iterations/2)-1));
                if (p + 1 == N){
                    System.out.println("P=1 == N, recalling function");
                    shors_algorithm(N);
                }
                else{
                    System.out.println("This is the " + iterations/2 + " transformation");
                    System.out.println(find_gcd(BigInteger.valueOf(p+1), BigInteger.valueOf(N)) + " and " + find_gcd(BigInteger.valueOf(p-1), BigInteger.valueOf(N)) + " are factors of " + N);
                }
            }
        }
    }

    public static void main(String[] args) {
        shors_algorithm(get_random_number(Integer.MIN_VALUE, Integer.MAX_VALUE));
    }
}