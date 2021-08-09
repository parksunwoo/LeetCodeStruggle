from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return anagrams.keys()
        
if __name__ == '__main__':
    # begin
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print (s.groupAnagrams(strs))
    
    
    
    
    
    
    
    
    
    
    
    
    