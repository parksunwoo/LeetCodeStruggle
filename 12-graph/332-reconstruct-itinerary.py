import collections
from typing import Collection, Optional, List
import itertools

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        # for a,b in sorted(tickets, reverse=True):
            # graph[a].append(b)
        
        # route = []
        # def dfs(a):
        #     while graph[a]:
        #         dfs(graph[a].pop())
        #     route.append(a)
            
        # dfs('JFK')
            
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']            
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        
        return route[::-1]
    
if __name__ == '__main__':
    sol = Solution()
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(sol.findItinerary(tickets))
