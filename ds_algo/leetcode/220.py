#!/usr/bin/env python3

# ## Algorithm:
# - Divide the entire lists into buckets
# - Since we wish to find numbers which are at most t apart from each other, the bucket size is set to t+1
# - Now, for each element in the list, we find which (t+1)-th size bucket does it fall into. Simple Remainder 
# - If there is already such a bucket, then we found our required pairs of numbers.
# - If not we check if there is a bucket before this which has a number which differs from the current number by atmost t.
# - If not we check if there is a bucket after this which has a number which differs from the current number by atmost t.
# - If none of the above is true, then we create the bucket for this number.
# - Since our elements can be atmost k apart from each other, we keep removing the first bucket once we have k buckets. 
#
# ## Time Complexity:
# - O(n) to run through the entire list
# - O(1) to add a bucket to the bucket dictionary
# - O(1) to remove the first bucket from the bucket dictionary
# - O(1) to find a bucket in the bucket dictionary
# - O(1) for all other arithmetic and comparison operations
# - Hence final time complexity is O(n)
#
# ## Code:
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # There is no difference between required indices of the elements in the list
        if k<1:
            return False
        buckets = {}
        width = t + 1
        for i, x in enumerate(nums):
            bucket_id = x // width
            if bucket_id in buckets:
                return True
            if bucket_id - 1 in buckets and abs(x - buckets[bucket_id - 1]) < width:
                return True
            if bucket_id + 1 in buckets and abs(x - buckets[bucket_id + 1] ) < width:
                return True
            buckets[bucket_id] = x
            if i >= k:
                del buckets[nums[i - k] // width]
        return False