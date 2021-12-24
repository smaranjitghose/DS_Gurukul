#!/usr/bin/env python3

# ## Algorithm:
#
# - Initialize a pointer curr to the head of the linked list. (Intuitively, it tells us where we are currently in the linked list) 
# - Initialize a pointer prev to a None (Intuitively, it tells us the previous element in the linked list)
# - Traverse through the linked list using the curr 
# - For each node, set the next pointer of the nodes to the node for prev pointer followed by updating prev pointer to point at the current node 
# - At the end of this traversal, the prev pointer will be pointing at the last node of initial linked list whose order has now been reversed. 
# - Thus the prev pointer points at the first element of the reverersed linked list. It can be considered as the new head of the linked list.
# - The curr pointer is now pointing at None which is initially the end of the original linked list.
# - Return the new head of the linked list i.e. the prev pointer.

# ## Time Complexity:
#
# - O(n) to traverse the entire linked list of n elements using the curr pointer
# - O(1) for all other arithmetic and comparison operations
# - Hence the total time complexity will be O(n)

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