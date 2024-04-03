class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        new=1
        while i<len(nums)-1:
            if nums[i]==0 and new<=len(nums)-1:
                if nums[new]!=0:
                    nums[i],nums[new]=nums[new],nums[i]
                else:
                    new+=1
            else:
                i+=1
                new+=1
                
       
        