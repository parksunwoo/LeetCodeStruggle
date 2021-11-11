import collections
from typing import Collection, Optional, List
import itertools
import heapq

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <=1 :
            return [0]
        
        
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        # print(graph)
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
                
        return leaves
                
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    n = 4
    edges = [[1,0],[1,2],[1,3]]
    sol = Solution()
    print(sol.findMinHeightTrees(n , edges))
    