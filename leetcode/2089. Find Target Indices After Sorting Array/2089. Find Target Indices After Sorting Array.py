https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        return l
        
