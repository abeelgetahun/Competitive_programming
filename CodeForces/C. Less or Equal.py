# this is("ab_el")
https://codeforces.com/problemset/problem/977/C
n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))
if k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print("-1")
elif k == n :
    print(arr[-1])
elif arr[k-1] == arr[k]:
    print("-1")
else:
    print(arr[k-1])
