class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        prefix_sum = 0
        count = 0
        print(prefix_sums,prefix_sum)
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum in prefix_sums:
                count += prefix_sums[prefix_sum]
                prefix_sums[prefix_sum] += 1
            else:
                prefix_sums[prefix_sum] = 1
        
        return count
