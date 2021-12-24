#!/usr/bin/env python3

# ## Algorithm:
#
# - Add a dummy node at the beginning to handle edge case of the left being 1
# - Set the anchor pointer to the dummy node
# - Set the curr pointer to the head
# - Traverse the linked list (left-1) times so that our anchor pointer is at the node before the (left-1)th node
# - Set a prev pointer to None 
# - Traverse the linked list using curr pointer (right-left+1) times
# - For each node, set the next pointer of the nodes to the node for prev pointer followed by updating prev pointer to point at the current node 
# - At the end of this traversal, the prev pointer will be pointing at the last node of initial sub-list whose order has now been reversed. 
# - Thus the prev pointer points at the first element of the reverersed sub-list.
# - The curr pointer is now pointing at the node after the rth node of the original linked list.
# - Also the end of the reversed sub-list (which is still pointed at by the next of the node of anchor pointer) needs to be connected to the node for the current pointer
# - We need to connect the node at the anchor pointer to beginning of the reversed sub-list. i.e. the node at the prev pointer.
# - The dummy node assists in dealing with an edge case of the left being 1
# - Return the new head of the linked list i.e. next pointer of the dummy node 
#     - If left > 1, then this will be the head
#     - If left = 1, then this will be the node at prev pointer
#
# ## Time Complexity:
# - O(left) to traverse the linked list upto the (left-1)th node using curr pointer
# - O(right-left+1) to traverse the linked list from the (left-1)th node upto the rth node using curr pointer
# - O(1) for all other arithmetic and comparison operations
# - If we assume, left + right + 1 ~ n, then the total time complexity will be O(n)
#
# ## Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == null or left == right:
            return head

        dummy = ListNode(-1, head)

        anchor = dummy
        curr = head 

        for i in range(left-1):
            anchor = curr
            curr = curr.next
        
        prev = None

        for i in range(right-left+1):
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        anchor.next.next = curr
        anchor.next = prev

        return dummy.next