class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        nums1.sort()   ; nums2.sort()
        top,below=0,0
        min_=max(len(nums1),len(nums2))
        while top<len(nums1) and below<len(nums2):
            if nums1[top]>nums2[below]:
                top-=1
            elif nums1[top]<nums2[below]:
                below-=1
            elif nums1[top]==nums2[below]:
                ans.append(nums1[top])
            below+=1
            top+=1 
        return ans
