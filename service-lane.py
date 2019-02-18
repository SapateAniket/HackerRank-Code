t=map(int,raw_input().split())
x,y=t[0],t[1]
n=map(int,raw_input().split())
for i in range(y):
    tmp=map(int,raw_input().split())
    i,j=tmp[0],tmp[1]
    fl=n[i:j+1]
    fl.sort()
    print fl[0]