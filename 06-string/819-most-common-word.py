import re
from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #paragraph = re.sub(r'"!?',;.', '', paragraph)
        # word_dict = Counter(paragraph.split(' '))
        
        # word_list = [k for k, v in word_dict.items() if k != banned[0]]
        # print(word_list)

        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = Counter(words)
        return counts.most_common(1)[0][0]
            


if __name__ == '__main__':
    # begin
    s = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print (s.mostCommonWord(paragraph=paragraph, banned=banned))