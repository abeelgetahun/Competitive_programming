#https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        place_holder=0
        seeker=0
        while seeker<len(nums):
            if nums[seeker]!=0 :
                nums[place_holder],nums[seeker]=nums[seeker],nums[place_holder]
                place_holder+=1
            seeker+=1

       
