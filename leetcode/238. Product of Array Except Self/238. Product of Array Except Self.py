class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left = [0] * n
        right = [0] * n
        left_product = 1
        for i in range(n):
            left[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            right[i] = right_product
            right_product *= nums[i]

        result = [left[i] * right[i] for i in range(n)]
        return result


