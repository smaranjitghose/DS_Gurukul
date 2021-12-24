#!/usr/bin/env python3

# ## Algorithm:
#
# - Declare an empty dictionary to store the indexes of each element which is already seen
# - Iterate through the list 
# - If the element is already seen and the difference between its previous and current index is <= k, then return True
# - Otherwise, add the element to the dictionary with its current index (or Update it's index)
#
# ## Time Complexity:
#
# - O(n) to run through the entire list
# - O(1) to add an element to the dictionary
# - O(1) to check if an element is present in the dictionary
# - O(1) for all other arithmetic and comparison operations
# - Hence the total time complexity is O(n)
#
# ## Code:


from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k<1:
            return False
        visited = defaultdict()
        for i,x in enumerate(nums):
            if x in visited and abs(visited[x]-i) <=k:
                return True
            else:
                visited[x] = i
        return False