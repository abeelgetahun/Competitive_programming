https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left,right=0,len(skill)-1
        skill.sort()
        ans=0
        sum_=(sum(skill)/(len(skill)/2))
        while left<right:
            if (sum_!=skill[left]+skill[right]):
                print(skill[left],skill[right])
                return -1
            left+=1 ; right-=1
        left,right=0,len(skill)-1
        while left<right:
            ans+=(skill[left]*skill[right])
            left+=1 ; right-=1
        return ans
         
