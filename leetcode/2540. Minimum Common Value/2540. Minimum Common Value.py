https://leetcode.com/problems/minimum-common-value/description/
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common=set(nums1).intersection(set(nums2))
        return min(common) if len(common)>0 else -1

        
