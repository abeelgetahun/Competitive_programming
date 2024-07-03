class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=100001
        n=len(nums)
        for i in range(n):
            l,r=i+1,n-1
            while l<r:
                sum_=nums[i]+nums[l]+nums[r]
                if abs(target-res)>abs(target-sum_) : res=sum_
                if (nums[i]+nums[l]+nums[r])>target:
                    r-=1
                elif (nums[i]+nums[l]+nums[r])<target:
                    l+=1
                else:
                    l+=1  ; r-=1
        return res
