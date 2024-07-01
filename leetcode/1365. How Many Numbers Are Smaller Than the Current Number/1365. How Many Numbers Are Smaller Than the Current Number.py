class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        value=[]
        sort_=sorted(nums.copy())
        for i in nums:
            value.append(bisect.bisect_left(sort_,i))
        return value
