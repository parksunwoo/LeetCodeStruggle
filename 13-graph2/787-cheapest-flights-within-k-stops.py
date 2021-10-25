import collections
from typing import Collection, Optional, List
import itertools
import heapq



class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w, in flights:
            graph[u].append((v,w))

        Q = [(0, src, K)]
        
        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        return -1

if __name__ == '__main__':
    sol = Solution()
    # n = 3
    # flights = [[0,1,100],[1,2,100],[0,2,500]]
    # src = 0
    # dst = 2
    # k = 1
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    print(sol.findCheapestPrice(n, flights, src, dst, k))
