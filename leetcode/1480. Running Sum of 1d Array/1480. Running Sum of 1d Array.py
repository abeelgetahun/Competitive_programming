class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        sum_=0
        for i in nums:
            sum_=sum_+i
            res.append(sum_)
        return res
        
