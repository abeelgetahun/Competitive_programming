#https://leetcode.com/problems/find-players-with-zero-or-one-losses/
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[]
        winer=[i[0] for i in matches]
        loser=[i[1] for i in matches]
        count=defaultdict(int)
        for i in loser:
            count[i]+=1
        ans2=[key for key,items in count.items() if items<2]
        ans1=list(set(winer)-set(loser))
        ans.append(sorted(ans1))
        ans.append(sorted(ans2))
        return ans
        
        
