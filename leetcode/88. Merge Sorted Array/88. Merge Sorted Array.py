#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r=len(nums1)-1
        for _ in range(len(nums2)):
            if r>=0 and nums1[r]==0:
                nums1.pop()
                r-=1
        nums1.extend(nums2)
        nums1.sort()
