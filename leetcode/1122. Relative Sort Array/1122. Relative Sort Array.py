class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]   ; arr1.sort()
        for i in arr2:
            j,n=0,len(arr1)
            while j<n:
                if i==arr1[j]:
                    ans.append(i)
                    arr1.pop(j)         ; j-=1  ; n-=1
                elif arr1[j]>i:
                    break
                j+=1   
        ans+=arr1
        return ans
