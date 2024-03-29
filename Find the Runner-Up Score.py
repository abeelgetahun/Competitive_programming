https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr =sorted(list( map(int, input().split())))
    if arr:
        y=arr[-1]
    for i in range(len(arr)-1,-1,-1):
        if y>arr[i]:
            print(arr[i])
            break
