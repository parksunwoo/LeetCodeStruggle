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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))
            
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            
            return node
    
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    sol = Solution()
    print(sol.buildTree(preorder, inorder))
    
    
    