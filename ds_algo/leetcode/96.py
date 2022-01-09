#!/usr/bin/env python3

# ## Algorithm:
# 
# - This problem can be simplified to catalan number sequence problem.
# - Let n be the number of nodes in the binary search tree while l and r are the number of nodes on the left and right of the root node.
#       - n = 0, 1 way of building a tree
#       - n = 1, 1 way of building a tree
#       - n = 2, 2 ways of building a tree
#             -  l=1,r=0 
#             -  l=0, r=2
#       - n = 3, 5 ways of building a tree 
#               - l=0,r=2 
#               - l=1,r=1 
#               - l=0,r=2
# - Thus we can confirm, that the given problem can be simplified to the catalan number sequence problem.
# 
# ## Time complexity:
#
# - O(n^2)
#
# ## Space complexity:
#
# - O(n), since we are using a list of size n+1 to store the catalan numbers
#
# ## Code:
