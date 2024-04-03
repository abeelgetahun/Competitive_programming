class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]+=nums[i]
                nums[i]=0
        for i in range(len(nums)):
            while nums[i-1]==0 and nums[i] and i>0: 
                nums[i-1],nums[i]=nums[i],nums[i-1]
                i-=1
        return nums

        
        