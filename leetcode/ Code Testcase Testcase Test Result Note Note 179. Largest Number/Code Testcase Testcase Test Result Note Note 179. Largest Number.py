#https://leetcode.com/problems/largest-number/description/
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                x=str(nums[j])*10
                y=str(nums[j+1])*10
                if x<y: 
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return "".join(str(nums).strip("[]").split(", ")) if nums[0]!=0 else "0"


        
