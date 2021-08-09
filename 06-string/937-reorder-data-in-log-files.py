from typing import List


class Solution(object):
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
            letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
        
if __name__ == '__main__':
    # begin
    s = Solution()
    #print (s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
    print (s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))