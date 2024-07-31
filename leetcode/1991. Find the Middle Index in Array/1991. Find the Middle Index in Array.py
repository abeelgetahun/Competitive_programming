class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        from_left_prefix=[0]*len(nums)
        prefix=0
        for i in range(len(nums)-1,-1,-1):
            prefix+=nums[i]
            from_left_prefix[i]=prefix
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix==from_left_prefix[i]:
                return i
        return -1
