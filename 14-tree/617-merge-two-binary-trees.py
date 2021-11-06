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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val, root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node
        else:
            return root1 or root2


if __name__ == '__main__':
    sol = Solution()
    root1 = [1,3,2,5]
    root2 = [2,1,3,null,4,null,7]
    print(sol.invertTree(root1, root2))