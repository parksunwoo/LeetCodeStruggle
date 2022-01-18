import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sol 1
        # for num in nums:
        #     if nums.count(num) > len(nums) //2 :
        #         return num

        # sol 2
        # counts = collections.defaultdict(int)
        # for num in nums:
            
        #     if counts[num] == 0:
        #         counts[num] = nums.count(num)
                
        #     if counts[num] > len(nums)//2:
        #         return num
            
        # sol 3
        # if not nums:
        #     return None
        
        # if len(nums) == 1:
        #     return nums[0]
        
        # half = len(nums) // 2
        # a = self.majorityElement(nums[:half])
        # b = self.majorityElement(nums[half:])
        
        # return [b, a][nums.count(a) > half]

        # sol 4
        return sorted(nums)[len(nums) // 2]
            
            
            
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums = [3,2,3]
    sol = Solution()
    print(sol.majorityElement(nums))
    
    
