class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        key=""
        first=strs[0]
        if strs:
            first=strs[0]
        for i in range(len(strs[0])):
            a=first[i]
            count=1
            for j in range(1,len(strs)):
                b=strs[j]
                if (b ) and len(b)>i and a==b[i]:
                    count+=1
            if count>=len(strs)  :
                key+=a
            else: 
                break
        return key