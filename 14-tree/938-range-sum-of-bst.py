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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # sol 1)
        # if not root:
        #     return 0
        # return (root.val if low <= root.val <= high else 0) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)                
        
        # sol 2)
        # def dfs(node: TreeNode):
        #     if not node:
        #         return 0

        #     if node.val < low:
        #         return dfs(node.right)
        #     elif node.val > high:
        #         return dfs(node.left)
        #     return node.val + dfs(node.left) + dfs(node.right)
        
        # return dfs(root)
        
        # sol 3)
        stack, sum = [root], 0
        
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                    
                if low <= node.val <= high:
                    sum += node.val
                    
        return sum
                    
        
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    root = [10,5,15,3,7,None,18]
    low = 7
    high = 15
    sol = Solution()
    print(sol.rangeSumBST(root, low, high))
    
    
    