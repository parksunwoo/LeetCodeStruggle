import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
            
        return result


# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [2,2,1]
    sol = Solution()
    print(sol.singleNumber(nums))
    