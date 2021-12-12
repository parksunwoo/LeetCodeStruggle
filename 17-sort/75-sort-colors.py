import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)
        
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    sol = Solution()
    print(sol.sortColors(nums))
    
    
    
