import collections
from tkinter import N
from turtle import left, right
from typing import Collection, Optional, List, Set

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
    
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp.popitem()[1]
            
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [1,2,3,1]
    # nums = [2,7,9,3,1]
    sol = Solution()
    print(sol.rob(nums))
