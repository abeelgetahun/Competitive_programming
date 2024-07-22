class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        inBasket=defaultdict(int)
        cnt=0
        l=0
        for r in range(len(fruits)):
            inBasket[fruits[r]]+=1
            while len(inBasket)>2:
                inBasket[fruits[l]]-=1
                if inBasket[fruits[l]]==0:
                    del inBasket[fruits[l]]
                l+=1
            cnt=max(cnt,len(fruits[l:r+1]))
        return cnt
