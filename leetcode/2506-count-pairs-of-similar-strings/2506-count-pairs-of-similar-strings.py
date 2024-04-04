class Solution:
    def similarPairs(self, words: List[str]) -> int:
        key=Counter()
        count=0
        for current_word in words:
            word="".join(sorted(set(current_word)))
            count+=key[word]
            key[word]+=1
        return count  