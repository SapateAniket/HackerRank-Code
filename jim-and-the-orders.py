t=int(raw_input())
ar=[0 for i in range(t)]
xe=[0 for i in range(t)]
for i in range(t):
    tmp[i]=map(int,raw_input().split())
    xe[i],cu,tm=tmp[0],tmp[0],tmp[1]
    ar[i]=cu+tm
    