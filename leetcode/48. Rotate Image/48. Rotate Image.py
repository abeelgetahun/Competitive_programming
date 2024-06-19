class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size=len(matrix)
        for i in range(size):
            temp=[]
            for j in range(size-1,-1,-1):
                temp.append(matrix[j][i])
            matrix.append(temp)
        for i in range(size):
            del matrix[0]
        
