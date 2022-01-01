#!/usr/bin/env python3




# ## Code:


def get_kth_prime(n:int)->int:

    # By Trial and Error, find the uppper bound of the state space
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
    
    # Ignore all composite numbers and get a list of prime numbers upto n
    prime_t = []
    for i in range(max_n):
        if is_prime[i]:
            prime_t.append(i)

    # Return the kth prime number
    return prime_t[n-1]   

