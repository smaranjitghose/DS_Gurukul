#!/usr/bin/env python3

## Algorithm:
#
# We have ZSUM = Z(n) + Z(n-1) - Z(n-2), where:
#        - Z(n) = S(n) + P(n)
#        - S(n) = 1^k + 2^k + 3^k + … + n^k
#        - P(n) = 1^1 + 2^2 + 3^3 + … + n^n
# The elements of Z(n-2) are also present in Z(n) and Z(n-1).  
# Hence, in ZSUM we effectively have the last element of Z(n) and Z(n-1)
# Therefore, ZSUM = (n^k + n^n) + ([n-1]^k + [n-1]^n) 
# Now for computing each component of this expression, we can use binary exponentiation.
#
# ## Time complexity:
# 
# - O(log((max(x,y)))))
#
# ## Space complexity:
#
# - O(1) since we are not using any extra space
#
# ## Code:

# To prevent overflow
M = 10**9+7

def bin_exp(x:int, y:int) -> int:
    if y == 0:
        return 1
    if y == 0:
        return x
    
    res = 1
    while y > 0:
        # If the power is odd, multiply the result with x
        if y & 1:
            res *= x%M
        # Square the base
        x *= x%M
        # Reduce the power by 2
        y >>= 1
    return res

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = bin_exp(n, k)
    b = bin_exp(n, n)
    c = bin_exp(n-1, k)
    d = bin_exp(n-1, n-1)