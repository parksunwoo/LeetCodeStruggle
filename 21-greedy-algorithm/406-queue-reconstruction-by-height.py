import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            print(person[1])
            print([-person[0], person[1]])
            result.insert(person[1], [-person[0], person[1]])
        return result
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    sol = Solution()
    print(sol.reconstructQueue(people))
    
    
    