#https://leetcode.com/problems/partition-labels/description/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_=0
        place_holder=0
        ans=[]
        while place_holder<=len(s):
            for seeker in range(len(s)-1,place_holder-1,-1):
                if s[place_holder]==s[seeker]:
                    max_=max(seeker,max_)
                    break
            if max_==place_holder:
                ans.append(max_+1)
            place_holder+=1
        for i in range(1,len(ans)):
            ans[i]=ans[i]-sum(ans[:i])

        return ans
