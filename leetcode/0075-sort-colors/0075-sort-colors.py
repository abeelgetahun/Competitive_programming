class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # this is ("ab_el")
        for i in range(len(nums)):
            j=i
            while nums[j-1]>nums[j] and j>0:
                nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1
        


       
            
        
        
        