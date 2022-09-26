# Shor's Facotring Algorithm: 
# Step 1: Decide whatever number you are interested in trying to factor
# Step 2: Declare a second number which is a number between 1 and N. 
# Step 3: The next step is to then find the GCD(N,K) – If GCD is not equal to one then the GCD is a factor of N else 
# if it is one you move on. 
# Step 3.1: If one, then you will need to find the smallest positive integer, r, such that f(x) = (k^x)mod N then f(a) = (a+r). 
# Now you will need to define another variable q, now you will need to find (qxk)mod N. 
# If the remainder is not one, then set the value of q to the value of the remainder that was calculated and repeat this step until
# the remainder is one; keeping track of the iterations of the recursion. 
# The number of transformations that you calculated 1…N will be the r use in the equation. 
# If r is an odd number go back to the second step, choosing a random number K. 
# Otherwise, define p = remainder in (r/2)th transformation – If p + 1 – N then go back to step two 
# otherwise move on to the final step of the algorithm. 
# Now you will be able to generate the factors of N by sampling doing f1 = GCD(p+1, N) and f2 = GCD(p-1, N)


import math
from random import Random, randint, random

def find_gcd(number_1, number_2):
    return math.gcd(number_1, number_2)

def shors_algorithm(number_to_factor):
    N = number_to_factor
    print("The number is: {}".format(N))
    K = randint(1, number_to_factor)
    print("The factor number is: {}".format(K))
    GCD = find_gcd(N, K)
    print("The GCD is {}".format(GCD))
    if GCD != 1:
        print("{} is a factor of {}".format(GCD, N))
    else:
        transformations = []
        q = 1
        iterations = 0
        while True:
            q = (q*K) % N
            transformations.append(q)
            iterations += 1
            print("This iteration, remainder, and N: {} {} {} {}".format(iterations, q, N, K))
            if q == 1:
                break
        if iterations % 2 != 0:
            print("Reloading here")
            shors_algorithm(N)
        else:
            p = transformations[int((iterations/2) -1)]
            print("This is p {}".format(p))
            if p + 1 == N:
                print("Reloading")
                shors_algorithm(N)
            else:
                print("This is the {} transformation".format(iterations/2))
                print("{} and {} are factors of {}".format(find_gcd(p+1, N), find_gcd(p-1,N), N))
        


if __name__ == "__main__":
    while True:
        shors = input()
        if shors == "break":
            break
        shors_algorithm(int(shors))