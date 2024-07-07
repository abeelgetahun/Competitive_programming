class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel="aeiou"
        res,sum_=0,0
        v=[]
        for i in range(len(s)):
            if s[i] in vowel:
                v.append(1)
            else:
                v.append(0)
        val=[]
        for i in range(len(v)):
            val.append(v[i])
            if (i-k)>=0 and v[i-k]==1:  
                val[i]-=1
        for k in val:
            sum_+=k
            res=max(res,sum_)
        return res
