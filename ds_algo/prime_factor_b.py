#!/usr/bin/env python3

## Algorithm:
#
# - Check if the number is divisible by 2 and find out all the powers of 2 which divide the number
# - Check if the number is divisible by 3 and find out all the powers of 3 which divide the number
# - Check if the number is divisble by the remaining prime numbers which are of the form 6k+1 or 6k-1
# - We also know that if (a,b) are factors of n, then either a or b should be less than sqrt(n)
# - Moreover, the next prime number after 2 and 3 is 5
# - Hence we start the loop from 5, iterate till sqrt(n), increment by 6 and check if the number is divisible by the given i or i+2

## Time Complexity: 
# 
# - O(sqrt(n))


def get_prime_factors(n:int)->list:
    
    prime_factors = []

    # Get all multiples of 2 if possible
    if n%2 ==0:
        count = 0
        while n%2 == 0:
            count += 1
            n = n/2
        prime_factors.append((2,count))
    
    # Get all multiples of 3 if possible
    if n%3 ==0:
        count = 0
        while n%3 == 0:
            count += 1
            n = n/3
        prime_factors.append((3,count))
    
    # Other than 2 and 3, all prime numbers are of the form 6k+1 or 6k-1
    i = 5
    while i*i <n:
        if n%i ==0:
            count = 0
            while n%i == 0:
                count += 1
                n = n/i
            prime_factors.append((i,count))
        if n%(i+2) ==0:
            count = 0
            while n%(i+2) == 0:
                count += 1
                n = n/(i+2)
            prime_factors.append((i+2,count))
        i += 6

    return prime_factors

# print(get_prime_factors(2500))