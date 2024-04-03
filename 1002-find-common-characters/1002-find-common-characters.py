class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word=words[0]
        char=""
        for i in word:
            count=1
            for j in range(1,len(words)):
                if i in words[j]:
                    words[j]=words[j].replace(i,"",1)
                    count+=1
            if count==len(words):
                char+=i
            word=word.replace(i,"",1)
        return char

                
