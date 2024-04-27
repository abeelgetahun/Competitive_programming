# this is ("ab_el")
test=int(input())
for _ in range(test):
    size=int(input())
    nums=list(map(int,input().split()))
    value=0
    sign=True if nums[0]>0 else False
    check=nums[0] ; left=0
    while left<len(nums):
        if sign:
            if nums[left]<0:
                sign=False
                value+=check
                check=nums[left]
                continue
            check=max(check,nums[left])
            left+=1
        if not sign:
            if nums[left]>0:
                sign=True
                value+=check
                check=nums[left]
                continue
            check=max(check,nums[left])
            left+=1
    print(value+check)
