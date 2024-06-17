class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered=[0]*52
        for x,y in ranges:
            covered[x]+=1
            covered[y+1]+=-1
        for i in range(1,len(covered)-1):
            covered[i]+=covered[i-1]
        for i in range(left,right+1):
            if covered[i]<1:
                return False
        return True
