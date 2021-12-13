import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
            
        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
            
        return result

# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    points = [[1,3],[-2,2]]
    k = 1
    
    points = [[3,3],[5,-1],[-2,4]] 
    k = 2
    sol = Solution()
    print(sol.kClosest(points, k))
    
    
    
