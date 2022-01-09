#!/usr/bin/env python3

# ## Algorithm:
#
# - This is quite straightforward.
# - We find the maximum and minimum elements in the array and use Euclidean algorithm to find the GCD of these two numbers.
#
# ## Time complexity:
# 
# - O(n) to compute the maximum element in the array
# - O(n) to compute the minimum element in the array
# - O(log(n)) to compute the gcd of the maximum and minimum element where n = max(a, b)
# - Hence the total time complexity is O(n)
#
# ## Space complexity:
# 
# - O(1) since we are not using any extra space
#
# ## Code:

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Find maximum number      
        a = float('-inf')
        for x in nums:
            if x > a:
                a = x
        # Find the minimum number
        b = float('inf')
        for x in nums:
            if x < b:
                b = x
        # Compute GCD:
        while b:
            a,b = b, a%b
        return a
