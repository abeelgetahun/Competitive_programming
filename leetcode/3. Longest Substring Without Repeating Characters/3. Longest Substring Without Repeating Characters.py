#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=[]
        max_=0
        for i in s:
            if i not in char:
                char.append(i)
                max_=max(max_,len(char))
            else:
                while i in char:
                    char.pop(0)
                char.append(i)
        return max_
                
