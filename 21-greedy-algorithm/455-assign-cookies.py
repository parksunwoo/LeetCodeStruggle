import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        # child_i = cookie_j = 0
        
        # while child_i < len(g) and cookie_j < len(s):
        #     if s[cookie_j] >= g[child_i]:
        #         child_i += 1
        #     cookie_j += 1
        # return child_i
        
        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
                
        return result
            
            
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    g = [1,2,3]
    s = [1,1]
    # g = [1,2]
    # s = [1,2,3]
    sol = Solution()
    print(sol.findContentChildren(g, s))
    