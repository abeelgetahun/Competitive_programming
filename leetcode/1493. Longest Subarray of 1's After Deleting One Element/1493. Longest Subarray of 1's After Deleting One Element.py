class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length=0
        count=1
        l,r=0,0
        while r<len(nums):
            if (nums[r]!=0 or count==1 ):
                if nums[r]==0 : count-=1
                r+=1
            else:
                while count==0:
                    if nums[l]==0:
                        count+=1
                        l+=1
                        break
                    l+=1
            length=max(length,(r-l-1))
        return length
