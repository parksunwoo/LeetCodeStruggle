import collections
from typing import Collection, Optional, List
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # results = []
        # prev_elements = []
        
        # def dfs(elements):
        #     if len(elements) == 0:
        #         results.append( prev_elements[:] )
                
        #     for e in elements:
        #         next_elements = elements[:]
        #         next_elements.remove(e)
                
        #         prev_elements.append(e)
        #         dfs(next_elements)
        #         prev_elements.pop()
        
        # dfs(nums)        
        # return results
        
        return list(itertools.permutations(nums))
        

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))
