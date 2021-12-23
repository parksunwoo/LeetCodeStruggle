import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        left, right = 0, len(nums) -1
        while left < right:
            mid = left + (right - left) //2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        pivot = left
        
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right - left) //2
            mid_pivot = (mid+pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    print(sol.search(nums, target))
    
    
    