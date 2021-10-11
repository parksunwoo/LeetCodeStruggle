import collections
from typing import Collection, Optional, List
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(itertools.combinations(range(1, n+1), k))
        
        results = []
        
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
                
            dfs([], 1, k)
            return results

if __name__ == '__main__':
    sol = Solution()
    n = 4
    k = 2
    print(sol.combine(n, k))
