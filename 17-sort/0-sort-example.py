import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys

class Solution:
    def bubblesort(A):
        for i in range(1, len(A)):
            for j in range(0, len(A)-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]

    # def quicksort(A, lo, hi):
    #     if lo < hi:
    #         pivot = partition(lo, hi)
    #         quicksort(A, lo, pivot -1)
    #         quicksort(A, pivot + 1, hi)
    
    # def partition(lo, hi):
    #     pivot = A[hi]
    #     left = lo
    #     for right in range(lo, hi):
    #         if A[right] < pivot:
    #             A[left], A[right] = A[right], A[left]
    #             left += 1
                
    #     A[left], A[hi] = A[hi], A[left]
    #     return left
    
    def quicksort(A, lo, hi):
        def partition(lo, hi):
            pivot = A[hi]
            left = lo
            for right in range(lo, hi):
                if A[right] < pivot:
                    A[left], A[right] = A[right], A[left]
                    left += 1
                    
            A[left], A[hi] = A[hi], A[left]
            return left
        
        
        if lo < hi:
            pivot = partition(lo, hi)
            quicksort(A, lo, pivot -1)
            quicksort(A, pivot + 1, hi)
            
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    sol = Solution()
    