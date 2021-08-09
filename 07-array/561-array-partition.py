from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # sum = 0
        # pair = []
        # nums.sort()
        
        # for n in nums:
        #     pair.append(n)            
        #     if len(pair) == 2:
        #         sum += min( pair )
        #         pair = []
        # return sum

        # for i, n in enumerate(nums):
        #     if i % 2 == 0:
        #         sum += n
        # return sum
    
        return sum(sorted(nums)[::2])
    
                    
        
                          
if __name__ == '__main__':
    # begin
    s = Solution()
    nums = [1,4,3,2]
    print (s.arrayPairSum(nums))
    
    
    
    


    
    
    
    