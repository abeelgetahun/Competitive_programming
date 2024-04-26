class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=len(p)
        p=Counter(p)
        ans=[]
        for i in range(len(s)-a+1):
            if Counter(s[i:a+i])==p:
                ans.append(i)
        return ans
