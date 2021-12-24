#!/usr/bin/env python3


# ## Algorithm:

# - Initialize a pointer curr to the head of the linked list. (Intuitively, it tells us where we are currently in the linked list) 
# - Initialize a pointer prev to a None (Intuitively, it tells us the previous element in the linked list)
# - Traverse through the linked list using the curr 
# - For every node, set it's next to the node pointed by prev while updating prev. (Initially prev points at None)
# - At the end, while curr points at a None value, the prev points at the last node of the initial linked list which has now the entire order reversed.
# - Thus making prev pointing at the first element of the new linked list or effectively being the new head.

# ## Time Complexity:

# - O(n) to traverse the entire linked list of n elements using the curr pointer

# ## Code:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        prev = None

        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        return prev