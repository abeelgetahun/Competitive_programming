class Solution:
    def smallestNumber(self, num: int) -> int:
        num=str(num)
        if int(num)<0:
            nums=[int(i) for i in num[1:]]
            nums.sort(reverse=True)
            return (int("".join(str(nums).strip("[]").split(", ")))*-1)
        elif int(num)>0:
            nums=[int(i) for i in num]
            nums.sort()
            i=1
            while nums[0]==0:
                if nums[i]!=0:
                    nums[0],nums[i]=nums[i],nums[0]
                i+=1
            return (int("".join(str(nums).strip("[]").split(", "))))
        else:
            return 0

        
