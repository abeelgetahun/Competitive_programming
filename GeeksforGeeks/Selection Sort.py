#https://www.geeksforgeeks.org/problems/selection-sort/1
#User function Template for python3
class Solution: 
    def select(self, arr, i):
        # code here 
        temp=i
        for j in range(i,len(arr)):
            if arr[j]<arr[temp]:
                temp=j
        arr[temp],arr[i]=arr[i],arr[temp]
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            self.select(arr,i)
        return arr

        
