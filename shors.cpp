#include "shors.h"
#include "math.h"
#include <iostream>
#include <algorithm>
#include <vector>

int find_gcd(int number_1, int number_2){
    return __gcd(number_1, number_2);
}


void shors_algorithm(int number_to_factor){
    int N = number_to_factor;
    int K = rand() % N + 1;
    int GCD = find_gcd(N, K);
    if (GCD != 1){
        cout << GCD << " is a factor of " << N;
    }
    else{
        vector<int> transformation;
        int q = 1;
        int iterations = 0;
        while (true){
            q = (q*K) % N;
            transformation.push_back(q);
            iterations++;
            if (q == 1){
                break;
            }
        }
        if (iterations % 2 != 0){
            cout << "Number of iterations is not even";
            shors_algorithm(N);
        }
        else{
            int p = transformation[int((iterations/2)-1)];
            if (p + 1 == N){
                cout << "P+1 == N, recalling function";
                shors_algorithm(N);
            }
            else{
                cout << "This is the " << iterations/2 << " transformation";
                cout << find_gcd(p+1, N) << " and " << find_gcd(p-1, N) << " are factors of " << N;
            }

        }
    }

}

int main (){
    int input = 0;
    do{
        cin >> input;
    }while (isdigit(input) == false);
    shors_algorithm(input);
    return 0;
}
