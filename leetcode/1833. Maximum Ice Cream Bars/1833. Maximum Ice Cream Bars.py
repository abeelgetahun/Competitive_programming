class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count_sort=[0]*max(costs)
        for i in costs:
            count_sort[i-1]+=1
        res=0
        for i in range(len(count_sort)):
            while count_sort[i]>0 and (coins-i-1)>=0:
                coins-=(i+1)
                count_sort[i]-=1
                res+=1
        return res
