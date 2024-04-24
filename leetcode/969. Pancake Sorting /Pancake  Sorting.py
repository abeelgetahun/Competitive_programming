class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        end = len(arr)
        for i in range(len(arr),0,-1):
            x = arr.index(i)
            arr1 = arr[:x+1][::-1]
            arr = arr1 + arr[x+1:]
            arr = arr[:end][::-1] + arr[end:]
            print("arr",arr)
            ans.append(x+1)
            ans.append(end)
            end -= 1
            print("ans",ans,i,end)
        return ans
