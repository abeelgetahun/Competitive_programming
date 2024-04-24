https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B
# this is ("ab_el")
a,b=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
ans=[]
def check(target):
    left,right=0,a
    while left<right:
        mid=(left+right)//2
        if arr1[mid]<target:
            left=mid+1
        else:
            right=mid
    ans.append(left)
for target in arr2 :
    check(target)
print(*ans)
    
