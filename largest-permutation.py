no=map(int,raw_input().split())
n,k=no[0],no[1]
arr=map(int,raw_input().split())
for i in range(k):
    ls=arr[i:]
    mx=max(ls)
    pos=arr.index(mx)
    tmp=arr[i]
    arr[i]=mx
    arr[pos]=tmp
for i in arr:
    print i,