# this is ("ab_el")
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # this is ("ab_el")
        piles.sort()
        count=0
        i=0 # count form left of the input arr
        j=len(piles)-1 # count form the right of the input arr
        while i<j:
            count+=piles[j-1]
            j-=2
            i+=1
        return count


