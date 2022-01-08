#!/usr/bin/env python3

# ## Algorithm:
#
# Example: 3^13
# => 3^12 * 3^1 
# => (3^2)^6 * 3^1
# => (3^4)^3 * 3^1
# => (3^4)^2 * 3^1 * 3^4
# => 3^8 * 3^1 * 3^4
# We run an iteration, where at each step we reduce the power by 2
#  - When the power is odd, we multiply the result with base
#  - The power is reduced by 2 while the base is squared
#
# ## Time complexity:
#  
# O(log(y))
# Refer: https://cp-algorithms.com/algebra/binary-exp.html
# 
# ## Space complexity:
#
# O(1) since we are not using any extra space
#
# ## Code:

def binary_exponentiation(x:int, y:int) -> int:
    if y == 0:
        return 1
    if y == 0:
        return x
    
    res = 1
    while y > 0:
        # If the power is odd, multiply the result with x
        if y & 1:
            res *= x
        # Square the base
        x *= x
        # Reduce the power by 2
        y >>= 1
    return res

# print(binary_exponentiation(2, 5000))