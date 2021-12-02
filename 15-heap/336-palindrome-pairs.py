import collections
from typing import Collection, Optional, List
import itertools
import heapq
import sys



class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    @staticmethod        
    def is_palindrome(word):
        return word == word[::-1]

    def insert(self, index:int, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
                
            node = node.children[char]
            node.val = char
        node.word_id = index


        
    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root
        
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
                    
                if not word[0] in node.children:
                    return result
                node = node.children[word[0]]
                word = word[1:]
                
        if node.word_id >= 0 and node.word_id != index:
           result.append([index, node.word_id])
           
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result



class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        
        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])

        return output


        
# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    words = ["abcd","dcba","lls","s","sssll"]
    sol = Solution()
    print(sol.palindromePairs(words))
    
    
    