import collections
from typing import Collection, Optional, List
import itertools
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1 
        
        return check(root) != -1
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    root = [3,9,20,null,null,15,7]
    sol = Solution()
    print(sol.isBalanced(root))
    