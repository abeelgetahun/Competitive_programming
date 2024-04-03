class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix=[]
        first=matrix[0]
        for i in range(len(first)):
            l=[first[i]]
            for j in range(1,len(matrix)):
                l.append(matrix[j][i])
            new_matrix.append(l)
        return new_matrix
                
        