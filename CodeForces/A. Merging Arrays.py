# this is ("ab_el")
a,b=map(int,input().split())
nums=list(map(int,input().split()))
nums2=list(map(int,input().split()))
merging=[]    ; i,j=0,0
while i < len(nums) or  j < len(nums2):
    if j == len(nums2) or  i < len(nums) and nums[i] < nums2[j]:
       merging.append(nums[i])
       i+=1
    else:
        merging.append(nums2[j])
        j+=1
print(*merging)
     
