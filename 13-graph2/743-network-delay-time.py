import collections
from typing import Collection, Optional, List
import itertools
import heapq



class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w, in times:
            graph[u].append((v,w))
            
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        
        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
                                
        if len(dist) == n:
            return max(dist.values())
        return -1

if __name__ == '__main__':
    sol = Solution()
    # times = [[2,1,1],[2,3,1],[3,4,1]]
    # n = 4
    # k = 2  
    # times = [[1,2,1]], n = 2, k = 1  
    times, n, k = [[1,2,1]], 2, 1
    print(sol.networkDelayTime(times, n, k))
