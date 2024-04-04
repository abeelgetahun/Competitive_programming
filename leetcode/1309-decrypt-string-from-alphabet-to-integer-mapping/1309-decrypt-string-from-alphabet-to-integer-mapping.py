# this is ("ab_el")
class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha=""
        s=list(s)
        i,y=0,len(s)
        # this part help to change each number to character list value separate using #
        while i<y:
            if s[i]=="#":
                temp=s[i-2]+s[i-1]
                s.pop(i-2)
                s.pop(i-1)
                s[i-2]=temp
                i-=2
                y-=2
            i+=1
        # this part used to covert list members to character (eg.a=97)
        for i in s:
            alpha+=chr(int(i)+96)
        return alpha

    
    


        
