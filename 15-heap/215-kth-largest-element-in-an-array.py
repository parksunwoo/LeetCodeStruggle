import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sol 1.
        # heap = list()
        # for n in nums:
        #     heapq.heappush(heap, -n)
            
        # for _ in range(k):
        #     heapq.heappop(heap)

        # return -heapq.heappop(heap)
    
        # sol 2.
        # heapq.heapify(nums)
        
        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)

        # return heapq.heappop(nums)
        
        # sol 3.
        # return heapq.nlargest(k, nums)[-1]
    
        # sol 4.
        return sorted(nums, reverse=True)[k-1]
        

        
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    # nums = [3,2,1,5,6,4]
    # k = 2
    
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    sol = Solution()
    print(sol.findKthLargest(nums, k))
    