import collections
from typing import Collection, Optional, List, Set
import itertools
import heapq
import sys
import bisect

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                
                counter.subtract(task)
                counter += collections.Counter()
                
            if not counter:
                break
            
            result += n - sub_count + 1
            
        return result


        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B"]
    n = 2    
    sol = Solution()
    print(sol.leastInterval(tasks, n))
    