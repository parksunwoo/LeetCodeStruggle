import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # sol1.
        # if root.left:
        #     self.minDiffInBST(root.left)
            
        # self.result = min(self.result, root.val - self.prev)
        # self.prev = root.val
        
        # if root.right:
        #     self.minDiffInBST(root.right)
            
        # return self.result

        # sol2.
        prev = -sys.maxsize
        result = sys.maxsize
        
        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            
            result = min(result, node.val - prev)
            prev = node.val
            
            node = node.right
        
        return result        
    
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    root = [4,2,6,1,3]
    sol = Solution()
    print(sol.minDiffInBST(root))
    
    
    