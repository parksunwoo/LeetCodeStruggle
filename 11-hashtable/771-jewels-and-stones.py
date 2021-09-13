import collections
from typing import Collection, Optional, List
import heapq

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 1
        # freqs = {}
        
        # for char in stones:
        #     if char not in freqs:
        #         freqs[char] = 1
                
        #     else:
        #         freqs[char] += 1
                
        # count = 0
        # for char in jewels:
        #     if char in freqs:
        #         count += freqs[char]
        
        # return count
        
        # 2
        # freqs = collections.defaultdict(int)        
        # count = 0
        
        # for char in stones:
        #     freqs[char] += 1
            
        # for char in jewels:
        #     count += freqs[char]
            
        # return count
        
        # 3
        # freqs = collections.Counter(stones)
        # count = 0
        # for char in jewels:
            # count += freqs[char]
            
        # return count
        
        # 4
        return sum(s in jewels for s in stones)
    
        
        
            
if __name__ == '__main__':
    sol = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    print(sol.numJewelsInStones(jewels, stones))
