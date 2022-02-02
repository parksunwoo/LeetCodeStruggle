import collections
from dataclasses import replace
from tkinter import N
from turtle import left, right
from typing import Collection, Optional, List, Set

class Solution:
    def secretmap(self, n: int, arr1: List[int],  arr2: List[int]) -> List[str]:
        maps = []
        for i in range(n):
            # print(bin(arr1[i] | arr2[i]))
            maps.append(
                bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace('1', '#')
                .replace('0', ' ')
            )
        return maps
            
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    sol = Solution()
    print(sol.secretmap(n, arr1, arr2))
