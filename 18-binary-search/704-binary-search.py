import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # sol 1.
        # def binary_search(left, right):
        #     if left <= right:
        #         mid = (left + right) // 2

        #         if nums[mid] < target:
        #             binary_search(mid+1, right)
        #         elif nums[mid] > target:
        #             binary_search(left, mid-1)
        #         else:
        #             return mid

        #     else:
        #         return -1
        
        # return binary_search(0, len(nums)-1)
        
        # sol 2.
        # left, right = 0, len(nums) -1
        # while left <= right:
        #     mid = (left + right) // 2
            
        #     if nums[mid] < target:
        #         left = mid + 1
                
        #     elif nums[mid] > target:
        #         right = mid - 1
                
        #     else:
        #         return mid
        
        # return -1
        
        # sol 3.
        # index = bisect.bisect_left(nums, target)
        # if index < len(nums) and nums[index] == target:
        #     return index
        # else:
        #     return -1
        
        # sol 4.
        try:
            return nums.index(target)    
        except ValueError:
            return -1
        
        
        

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9    
    sol = Solution()
    print(sol.search(nums, target))
    