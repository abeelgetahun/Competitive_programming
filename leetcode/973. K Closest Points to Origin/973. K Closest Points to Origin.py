class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # "index of points" : "ditance of points from the origin"
        distance={}
        for i in range(len(points)):
            d=((points[i][0]**2)+(points[i][1]**2))**0.5
            distance[i]=[d,points[i]]
        z=dict(sorted(distance.items(), key=lambda x:x[1]))
        res=[]
        for key,val in z.items():
            if k<1:  break
            res.append(val[1])
            k-=1            
        return res 
