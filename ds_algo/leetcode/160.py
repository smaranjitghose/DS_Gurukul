#!/usr/bin/env python3

# ## Algorithm:
#
# - Declare two temporary pointers that point at the respective heads of the linked Lists A and B
# - Traverse both the linked lists using these two pointers (separately) to compute the length of the linked lists A and B respectively
# - Initialize currA and currB pointers to the respective heads of the linked lists A and B 
# - Compute the difference d lengths of the linked lists A and B
# - If the d>0 (implying linked list A is longer), then move the currA pointer d times ahead 
# - If the d<0 (implying linked list B in longer), then move the currB pointer d times ahead
# - Now, traverse the linked lists simultaneously using the currA and currB pointers until currA and currB pointers are equal
# - Return the pointer currA:
#    - If the interection point is found, the currA pointer will be pointing at the intersection point
#    - If the interection point is not found, the currA pointer will be pointing at the end of the linked list, i.e. None
#
# ## Time Complexity:
#
# - O(n) to find the length of the linked list A
# - O(m) to find the length of the linked list B
# - O(n-m) to shift the pointer of the longer linked list such that both pointers traverse the same length 
# - O(m) to traverse the shorter list and the remainder of the longer list
# - O(1) for all other arithmetic and comparison operations
# - If we assume that m-n ~ n, then the total time complexity is O(n)
#
# ## Space Complexity:
#
# - O(1)
#
# ## Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        currA, currB = headA,headB
        tempA, tempB = headA, headB
        
        l_A, l_B = 0,0
        
        while tempA:
            tempA = tempA.next
            l_A+= 1
        
        while tempB:
            tempB = tempB.next
            l_B+= 1
        
        d = l_A -l_B
        
        
        if d>0:
            for i in range(abs(d)):
                currA = currA.next
        elif d<0:
            for i in range(abs(d)):
                currB = currB.next
        
        while currA is not currB:
            currA = currA.next
            currB = currB.next

        return currA