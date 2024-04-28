#https://leetcode.com/problems/maximum-average-subarray-i/description/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        sum_ = sum(nums[:k])
        max_= sum_ 
        while r < len(nums):
            sum_ = sum_ - nums[l] + nums[r]  
            max_ = max(max_, sum_)
            l += 1 ; r += 1
        return max_ / k
