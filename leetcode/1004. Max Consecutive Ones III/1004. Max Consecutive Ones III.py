#https://leetcode.com/problems/max-consecutive-ones-iii/description/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        zero_count = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[l]==0:
                    zero_count -= 1
                l += 1
            max_length = max(max_length,r-l+1)
        return max_length
