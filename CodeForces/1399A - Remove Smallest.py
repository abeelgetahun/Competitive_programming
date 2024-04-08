 # this is ("ab_el")
def remove_smallest(x):
    l,r=0,1
    while len(x)>1:
        if x[l]==x[r]:
            x.remove(x[l])
        elif abs(x[l]-x[r])>1:
            return False
        else:
            x.remove(min(x[r],x[l]))
    return True
if __name__=="__main__":
    test=int (input())
    for _ in range(test):
        a=int(input())
        b=sorted(list(map(int,input().split())))
        print("YES" if remove_smallest(b)==True else "NO")
