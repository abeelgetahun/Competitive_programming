class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        ans=0
        for i in range(len(points)):
            ans=max(points[i][0]-points[i-1][0],ans)
        return ans
