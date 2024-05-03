class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cumulative_sums = {0: 1}
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum - k in cumulative_sums:
                res += cumulative_sums[current_sum - k]
            cumulative_sums[current_sum] = cumulative_sums.get(current_sum, 0) + 1
        return res
