class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3 or arr[0]>arr[1]:
            return False
        i=0
        for y in range(1,len(arr)):
            if arr[y-1]>arr[y]:
                i=y  ; break
        for x in range(1,len(arr)):
            if x<i and arr[x-1]>=arr[x]:
                return False
            elif x>i and arr[x]>=arr[x-1]:
                return False
        return True
