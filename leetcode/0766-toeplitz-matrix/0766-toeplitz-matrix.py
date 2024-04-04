class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        a=len(matrix)
        b=len(matrix[0])
        for i in range(a-1):
            for j in range(b):
                temp=matrix[i][j]
                x,y=i,j
                for k in range(a):
                    x+=1
                    y+=1
                    if x>=a or y>=b:
                        continue
                    if temp!=matrix[x][y]:
                        return False
        return True

