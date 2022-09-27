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

# Helper function, calls gcd function to find the gcd between two numbers
def find_gcd(number_1, number_2):
    return math.gcd(number_1, number_2)

# Shor's Algorithm implemented in the below function
def shors_algorithm(number_to_factor):
    # The Number that is trying to be factored
    N = number_to_factor
    print("The number is: {}".format(N))
    # The Number we are utilizing to find factors of N
    K = randint(1, number_to_factor)
    print("The factor number is: {}".format(K))
    # Calling the gcd helper function to find the gcd
    GCD = find_gcd(N, K)
    print("The GCD is {}".format(GCD))
    # If the GCD returned is not one, that number is a factor of N
    if GCD != 1:
        print("{} is a factor of {}".format(GCD, N))
    else:
        # Otherwise, we have to step into Shor's Algorithm
        # Initialize an array to hold the results of the transformation, a variable q and the number of times the transformation was conducted
        transformations = []
        q = 1
        iterations = 0
        # Perform the transformation sequence until the remainder is one
        while True:
            q = (q*K) % N
            transformations.append(q)
            iterations += 1
            print("This iteration, remainder, N, and factor: {} {} {} {}".format(iterations, q, N, K))
            if q == 1:
                break
        # If the number of iterations is odd then we have to redo the algorithm with a different K value
        if iterations % 2 != 0:
            print("Number of Iterations is not even")
            shors_algorithm(N)
        else:
            # We now grab the result of the iterations/2 th transformation
            p = transformations[int((iterations/2) -1)]
            print("This is p {}".format(p))
            # if the P + 1 is equal to the N then we have to redo the algorithm with a different K value
            if p + 1 == N:
                print("P + 1 == N, recalling function")
                shors_algorithm(N)
            else:
                # Otherwise, we identify the transformation
                print("This is the {} transformation".format(int(iterations/2)))
                # Utilizing the gcd function, with P-1 and P+1 will return 2 factors of the number N
                print("{} and {} are factors of {}".format(find_gcd(p+1, N), find_gcd(p-1,N), N))
        


if __name__ == "__main__":
    while True:
        shors = input()
        if shors == "break":
            break
        shors_algorithm(int(shors))