import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sol 1.
        # if not nums:
        #     return nums
        
        # r = []
        # for i in range (len(nums)- k +1):
        #     r.append(max(nums[i:i+k]))
        # return r
        
        #sol 2.
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue
            
            if current_max == float('-inf'):
                current_max  = max(window)
            elif v > current_max:
                current_max = v
                    
            results.append(current_max)
            
            if current_max == window.popleft():
                current_max = float('-inf')
                
        return results

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))
    