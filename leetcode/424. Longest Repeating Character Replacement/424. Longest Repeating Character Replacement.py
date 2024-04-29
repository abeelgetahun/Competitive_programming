class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_char={}
        left=0
        max_=0
        for right in range(len(s)):
            if s[right] in count_char:
                count_char[s[right]]+=1
            else:
                count_char[s[right]]=1
            while right-left+1-(max(count_char.values()))>k:
                count_char[s[left]]-=1
                left+=1
            max_=max(max_,right-left+1)
        return max_
