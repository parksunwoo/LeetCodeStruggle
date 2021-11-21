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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1 :])
        
        return node
    
            
                
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    sol = Solution()
    print(sol.sortedArrayToBST(nums))
    