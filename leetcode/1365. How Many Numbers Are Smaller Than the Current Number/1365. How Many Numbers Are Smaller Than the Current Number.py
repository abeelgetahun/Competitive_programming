class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copy=sorted(nums.copy())
        value=[]
        for i in nums:
            y=copy.index(i)
            value.append((len(copy[:y])))
        return(value)
        
