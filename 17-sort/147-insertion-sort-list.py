import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
                
        return merged
        
        
        
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print(sol.merge(intervals))

    
    