class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total=0
        stack=[]
        for i in arr:
            if not stack:
                stack.append([i,1,0])
            else:
                count=0
                while stack and stack[-1][0]>i:
                    a,b,c=stack.pop()
                    total+=(a*(count+b))+(count*c*a)
                    count+=b
                stack.append([i,1+count,count])
        count=0
        while stack:
            a,b,c=stack.pop()
            total+=(a*(count+b))+(count*c*a)
            count+=b
        m=(10**9)+7
        return total%m
