import collections
from dataclasses import replace
from tkinter import N
from turtle import left, right
from typing import Collection, Optional, List, Set

class Solution:
    def shuttle(self, n:int, t:int, m:int, timetable:List[str]) -> str:
        # n : 셔틀운행횟수
        # t : 셔틀운행간격
        # m : 한 셔틀에 탈 수 있는 최대 크루 수
        
        timetable = [
            int(time[:2]) * 60 + int(time[3:]) for time in timetable
        ]
        timetable.sort()
        current = 540
        
        for _ in range(n):
            for _ in range(m):
                if timetable and timetable[0] <= current:
                    candidate = timetable.pop(0) - 1
                else:
                    candidate = current
                    
            current += t

        h, m = divmod(candidate, 60)
        return str(h).zfill(2) + ':' + str(m).zfill(2)

            
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    n = 2
    t = 10
    m = 2
    timetable = ["09:10", "09:09", "08:00"]
    sol = Solution()
    print(sol.shuttle(n, t, m, timetable))
