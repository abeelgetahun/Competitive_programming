#https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort(reverse=True)
        count=0
        left,right=0,len(trainers)-1
        while left<len(players) and right>-1:
            if players[left]<=trainers[right]:
                count+=1
                left+=1 ; right-=1 
            else:
                right-=1
        return count
