#!/usr/bin/env python3

# ## Algorithm:
#
# - If the number is 1 or 0, then it is not prime
# - If the number is 2 or 3, then it is prime
# - Thus multiples of 2 and 3 are not prime
# - Now, we know that for any number n having two factors a and b such that a*b = n, a is always <= sqrt(n) and b is always >= sqrt(n) [Vice Verse]
# - Hence, we need not check for all numbers from 3 to n, if we are able to find a factor of n less than sqrt(n) 
# - Now, we can observe that other than 2 or 3, all prime numbers are of the form 6k+1 or 6k-1
#    - 5 = 6*1 - 1
#    - 7 = 6*1 + 1
#    - 13 = 6*2 + 1
#    - 11 = 6*2 - 1
#    - 17 = 6*3 - 1
#    - 19 = 6*3 + 1
# So if we start from 5 and check if that number and the number two places away from it divides n, then we can move in steps of 6 instead of 1
#
# ## Time Complexity:
#
# - All comparisons and arithmetic operations are O(1)
# - The loop and all operations inside it takes a total of  upto ~ < sqrt(n) to compelete (since we are incrementing by 6 instead of 1) 
# - (This can be expressed in a better form) 
# - Hence overall time compexity can be expressed as O(sqrt(n))
#
# ## Space Complexity:
# 
# - O(1) since we are not using any extra space
#
# ## Code:

from math import sqrt


def check_prime(n):
    if n<2:
        return False 
    if n==2 or n==3:
        return True 
    if n%2 ==0 or n%3==0:
        return False 
    for i in range(5,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True 

T=int(input())
for _ in range(T):
    
    N=int(input())
    if check_prime(N):
        print("yes")
    else:
        print("no")
