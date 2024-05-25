class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        total_passenger=[0]*1001
        for numpassenger,initial,final in trips:
            total_passenger[initial]+=numpassenger
            total_passenger[final]-=numpassenger
        check=0
        for i in total_passenger:
            check+=i
            if check>capacity:
                return False
        return True
        
