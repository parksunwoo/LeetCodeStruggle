import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s, t))


