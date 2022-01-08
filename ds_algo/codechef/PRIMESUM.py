  #!/usr/bin/env python3

# ## Algorithm:
#
# - This is a classic application of Sieve of Eratosthenes. If you want a better visualzation of the algorithm, refer to Khan Academy's [video](https://www.youtube.com/watch?v=klcIklsWzrY).
# - We declare an upper bound of the state space: max_n = 2*10^6
# - Declare an empty list of boolean values of the size max_n and initialize it to True for all elements.  This means we initially consider all the numbers uptil n to be prime
# - Now, as we already know that 0 and 1 are not prime, we can set the first two elements to False
# - Now, we can start iterating through the list and check if the number is prime or not
# - If the number is prime, then we know that it's mutiples upto max_n are composite. Hence we set them to False
# - If we have already checked all numbers upto sqrt(max_n), then we need not go further
# - Since all the multiples of all the numbers before x (when x is prime) are already set to False, we just have to check for multiples of x from x*x.
#     - For example: 
#     - For 5, it's multiples 5*2 and 5*3 were already set to False when checking for the multiples of 2 and 3 (which are less than 5). 
#     - Hence we start assiging False to multiples of 5 from 5*5.   
# - Now, we declare another empty list of size max_n and initialize it to 0 for all elements.
# - We can start iterating through the list and populate the list with the sum of all prime numbers upto n.
# - Now, for each pair of l and r,it is a simple lookup in the list to get the sum of all prime numbers between l and r.
#
# ## Time Complexity:
#
# - O(nlog(log(n))) 
# - Reference: https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
#
# ## Space Complexity:
#
# - O(n): To create the list of boolean values of size n indicating whether the ith number is prime or not
# - O(n): To create the list of sum of prime numbers upto n
# - Although a list of n elements is required, using a list of boolean values instead of a list of integers saves space as bool occupies less memory than int. This is very significant for implementation in other programming languages like C++. 
# - Hence the overall space complexity is O(n)


# ## Code:

max_n = 9*10**6
# Declare a list of bool values of size max_n
is_prime = [True]*max_n
# We already know that 0 and 1 are not prime
is_prime[0], is_prime[1] = False,False
# Perfome Sieve of Eratosthenes till sqrt(max_n)
i = 2
while i*i < max_n:
    if is_prime[i]:
        for j in range(i*i, max_n, i):
            is_prime[j] = False
        i += 1
# Declare a list of sum for all prime numbers upto n where n<=max_n
prime_sum = [0]*max_n
running_sum = 0
# Now, populate the prime_sum list with the sum of all prime numbers upto n
for i in range(2,max_n):
    if is_prime[i]:
        running_sum += i
    prime_sum[i] = running_sum

T = int(input())
for _ in range(T):
    l = int(input())
    r = int(input())
    print(prime_sum[r]-prime_sum[l-1])
