class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        max=(len(numbers)-1)
        min=0
        while max>min:
            sum=numbers[min]+numbers[max]
            if sum<target:
                min+=1
            elif sum>target:
                max-=1
            else :
                return [min+1,max+1]
                   
