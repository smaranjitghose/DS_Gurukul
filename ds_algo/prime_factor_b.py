#!/usr/bin/env python3

# ## Algorithm:
#
# - If n is less than 2, it has no prime factors
# - Check if the number is divisible by 2 and find out all the powers of 2 which divide the number
# - Check if the number is divisible by 3 and find out all the powers of 3 which divide the number
# - Now, all other prime numbers are of the form 6k+1 or 6k-1 starting from 5
# - Futhermore, we know that if (a,b) are factors of n, then either a or b should be less than sqrt(n)
#    - 5 = 6*1 - 1
#    - 7 = 6*1 + 1
#    - 13 = 6*2 + 1
#    - 11 = 6*2 - 1
#    - 17 = 6*3 - 1
#    - 19 = 6*3 + 1
# - Hence we check if number has any other prime factors less than sqrt(n)
# - If the number after being divided by all it's factor less than sqrt(n) is greater than 2, then it is a prime number and a factor of itself
# - Return the number of prime factors
#
# ## Time Complexity: 
# 
# - O(sqrt(n))
#
# ## Space Complexity:
#
# - O(1) since we would be having a constant number of prime factors for any number [**Need to check**]
#
# ## Code:

def get_prime_factors(n:int)->list:

    if n <2:
        return []
    
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
    
    if n>2:
        prime_factors.append((n,1))

    return prime_factors

# print(get_prime_factors(3600))