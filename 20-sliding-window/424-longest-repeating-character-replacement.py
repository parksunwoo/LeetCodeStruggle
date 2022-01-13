import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =  right = 0
        counts = collections.Counter()
        
        for right in range(1, len(s) + 1):
            counts[s[right-1]] += 1
            max_char_n = counts.most_common(1)[0][1]
            
            # print(counts.most_common(1)[0])
            
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        
        return right - left
    
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    # s = "ABAB"
    # k = 2
    s = "AABABBA"
    k = 1
    sol = Solution()
    print(sol.characterReplacement(s, k))
    