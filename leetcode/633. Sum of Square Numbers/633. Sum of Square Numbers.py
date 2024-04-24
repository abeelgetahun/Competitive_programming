#https://leetcode.com/problems/sum-of-square-numbers/description/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left,right=0,int(c**0.5)
        while left<=right:
            sum=left**2+right**2
            if sum==c:
                return True
            elif sum<c:
                left+=1
            else:
                right-=1
        return False
