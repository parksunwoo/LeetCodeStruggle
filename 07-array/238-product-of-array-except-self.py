from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums)-1, 0-1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
                          
if __name__ == '__main__':
    # begin
    s = Solution()
    nums = [1,2,3,4]
    print (s.productExceptSelf(nums))
    
    
    