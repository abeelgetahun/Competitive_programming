class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        reverse=[]
        for i in image:
            reverse.append(i[::-1])
        inverse=[]
        for i in reverse:
            temp=[]
            for x in i:
                temp.append(1 if x==0 else 0)
            inverse.append(temp)
        return inverse
