from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for num in nums:            
        #     remain = target - num
        #     if nums.index(remain) > 0 :
        #         return [nums.index(num), nums.index(remain)]
            
        # for i, n in enumerate(nums):
        #     complement = target - n            
        #     if complement in nums[i+1:]:
        #         return nums.index(n), nums[i+1:].index(complement) + (i+1)
        
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target- num]:
                return nums.index(num), nums_map[target- num]
        
if __name__ == '__main__':
    # begin
    s = Solution()
    # nums = [2,7,11,15]
    # target = 9
    
    # nums = [3,2,4]
    # target = 6
    
    nums = [3,3]
    target = 6
    print (s.twoSum(nums, target))