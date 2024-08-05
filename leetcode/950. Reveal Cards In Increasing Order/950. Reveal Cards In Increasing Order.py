class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        que=collections.deque(range(len(deck)))
        res=[0]*len(deck)
        for i in deck:
            x=que.popleft()
            res[x]=i
            if que:
                que.append(que.popleft())


        return res
        
