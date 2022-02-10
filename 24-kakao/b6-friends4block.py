import collections
import re
from dataclasses import replace
from typing import Collection, Optional, List, Set

class Solution:
    def block(self, m: int, n: int, board:List[str]) -> int:
        board  = [list(x) for x in board]
        # 일치 여부를 찾는 것
        matched = True
        while matched:
            matched = []
            for i in range(m - 1):
                for j in range(n - 1):
                    if board[i][j] == board[i][j+1] == board[i+1][j+1] == board[i+1][j] != '#':
                        matched.append([i, j])

            # 일치한 위치를 삭제
            for i, j in matched:
                board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = '#'
            
            # 빈 공간에 위에 있는 블록을 아래로 떨어뜨리는 처리
            for _ in range(m):
                for i in range(m-1):
                    for j in range(n):
                        if board[i+1][j] == '#':
                            board[i+1][j], board[i][j] = board[i][j], '#'
                
        return sum( x.count('#') for x in board)


        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    sol = Solution()
    print(sol.block(m, n, board))


