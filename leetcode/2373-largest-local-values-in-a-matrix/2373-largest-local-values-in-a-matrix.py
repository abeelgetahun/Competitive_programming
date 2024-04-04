class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        matrix=[]
        n=len(grid)-2
        for i in range(n):
            b=[]
            for j in range(n):
                a=[]
                for k in range(3):
                    a.extend(grid[i+k][j:j+3])
                b.append(max(a))
            matrix.append(b)
        return matrix