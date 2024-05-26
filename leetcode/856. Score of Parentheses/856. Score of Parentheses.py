class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res=0    ; balanced=0
        for i in range(len(s)):
            if s[i]=="(":
                balanced+=1
            elif s[i]==")":
                balanced-=1
                if i>0 and s[i-1]=="(":
                    res+= 2**balanced
        
        return res
