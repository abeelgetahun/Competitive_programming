class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge=""
        word1=deque(list(word1)) ; word2=deque(list(word2))
        while word1 or word2:
            if word1>=word2:
                merge+=word1.popleft()
            if word1<word2:
                merge+=word2.popleft()
        return merge
