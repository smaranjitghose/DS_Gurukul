#!/usr/bin/env python3

# ## Algorithm:
# - Initialize an empty set to store the already visited elements
# - Iterate through the list
# - If the current element is in the set, return True 
# - Otherwise, add the element to the set
#
# ## Time Complexity: 
# - O(n) to run through the entire list
# - O(1) to add an element to the set
# - O(1) to check if an element is present in the set
# - Hence final time complexity is O(n)
# 
# ## Code:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)
        return False
        