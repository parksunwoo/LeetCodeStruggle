import collections
from typing import Collection, Optional, List
import itertools
import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
            
        return root
          
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    sol = Solution()
    print(sol.bstToGst(root))
    