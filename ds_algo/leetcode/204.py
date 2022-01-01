#!/usr/bin/env python3

# ## Algorithm:
#
#
# - This is a classic application of Sieve of Eratosthenes. If you want a better visualzation of the algorithm, refer to Khan Academy's [video](https://www.youtube.com/watch?v=klcIklsWzrY).
# - If n is less than 2, no prime numbers are possible
# - Declare an empty list of boolean values of the size n and initialize it to True for all elements.  This means we initially consider all the numbers uptil n to be prime
# - Now, as we already know that 0 and 1 are not prime, we can set the first two elements to False
# - Now, we can start iterating through the list and check if the number is prime or not
# - If the number is prime, then we know that it's mutiples upto n are composite. Hence we set them to False
# - If we have already checked all numbers upto sqrt(n), then we need not go further
# - Since all the multiples of all the numbers before x (when x is prime) are already set to False, we just have to check for multiples of x from x*x.
#     - For example: 
#     - For 5, it's multiples 5*2 and 5*3 were already set to False when checking for the multiples of 2 and 3 (which are less than 5). 
#     - Hence we start assiging False to multiples of 5 from 5*5.   
# - Once we have the entire list of bool values indicating which numbers upto to n are prime or not,  we simply find the sum of truth values to get the count of primes till n.
# 
# ## Time Complexity:
#
# - O(nlog(log(n))) 
# - Reference: https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
#
# ## Space Complexity:
#
# - O(n): To create the list of boolean values of size n indicating whether the ith number is prime or not
#
# ## Code 

from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        
        is_prime = [True]*n
        is_prime[0], is_prime[1] = False,False
        
        for i in range(2,int(sqrt(n))+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        return sum(is_prime)

## Note:
# 
# - In our solution, we have to compute square root of n which might be expensive for large values of n
# - We can improve upon this by slightly modifying the termination conditon for the loop:
#         - Given, i < sqrt(n)
#         - Squaring both sides we get i*i <=n
# - This would not affect the remainder of the code as the increment remains the same.

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        
        is_prime = [True]*n
        is_prime[0], is_prime[1] = False,False

        i = 2

        while i*i < n:
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
            i += 1
        
        return sum(is_prime)