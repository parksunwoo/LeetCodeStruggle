import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys



class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # if char not in node.children:
                # node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)      
        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    # nums = [3,2,1,5,6,4]
    # k = 2
    
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    sol = Solution()
    print(sol.findKthLargest(nums, k))
    