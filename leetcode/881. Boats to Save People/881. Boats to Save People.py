https://leetcode.com/problems/boats-to-save-people/description/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        min_numBot=0
        left,right=0,len(people)-1
        people.sort()
        while left<=right:
            remain=limit-people[right]
            if remain>=people[left]:
                left+=1
            min_numBot+=1
            right-=1
        return min_numBot
