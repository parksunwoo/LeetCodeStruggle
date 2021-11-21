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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        #     return root
        # return None
        
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
                
        return root
    
        
if __name__ == '__main__':
    sol = Solution()
    root = [4,2,7,1,3,6,9]
    print(sol.invertTree(root))
