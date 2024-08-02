class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[0]*(n+1)
        for first,last,seat in bookings:
            arr[first-1]+=seat
            arr[last]-=seat
        prefix=0
        for i in range(len(arr)):
            prefix+=arr[i]
            arr[i]=prefix
        return arr[:-1]
