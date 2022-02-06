import collections
from dataclasses import replace
from tkinter import N
from turtle import left, right
from typing import Collection, Optional, List, Set

class Solution:
    def cache(self, cacheSize:int, cities:List[str]) -> int:
        cache = collections.deque(maxlen=cacheSize)
        elapsed: int = 0
        
        if cacheSize == 0:
            return len(cities) * 5 
        
        for c in cities:
            c = c.lower

            if c in cache:
                cache.remove(c)
                cache.append(c)
                elapsed += 1
            else:
                cache.append(c)
                elapsed += 5
                
        return elapsed
            
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    sol = Solution()
    print(sol.cache(cacheSize, cities))
