import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result : Set = set()

        #sol1
        # nums2.sort()
        # for n1 in nums1:
        #     i2 = bisect.bisect_left(nums2, n1)
        #     if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
        #         result.add(n1)
        # return result
    
        #sol2
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        
        return result                

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    sol = Solution()
    print(sol.intersection(nums1, nums2))
    
    
    