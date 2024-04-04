class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowel=set("aeiouAEIOU")
        i,j=0,len(s)-1
        while i<j:
            if s[i] not in vowel:
                i+=1
            elif s[j] not in vowel:
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
       
        return "".join(s)

        