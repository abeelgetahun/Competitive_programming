#https://leetcode.com/problems/minimum-common-value/
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        u=set(nums1).intersection(set(nums2))
        u=list(u)
        return min(u) if len(u)>0 else -1

        
