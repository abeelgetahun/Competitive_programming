class Solution:
    def sortSentence(self, s: str) -> str:
        sorted_=[0]*len(s.split())
        for i in s.split():
            y=int(i[-1])-1
            sorted_[y]=i[:-1]
        return " ".join(sorted_)
