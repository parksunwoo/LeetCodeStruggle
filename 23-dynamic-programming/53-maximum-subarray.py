import collections
import sys
from tkinter import N
from turtle import left, right
from typing import Collection, Optional, List, Set

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sol 1
        # for i in range(1, len(nums)):
        #     nums[i] += (nums[i-1] if nums[i-1] > 0 else 0)
        # return max(nums)
        
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
            
        return best_sum

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    print(sol.maxSubArray(nums))


