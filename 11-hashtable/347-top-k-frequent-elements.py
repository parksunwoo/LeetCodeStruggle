import collections
from typing import Collection, Counter, Optional, List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
        
            
if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(sol.topKFrequent(nums, k))
