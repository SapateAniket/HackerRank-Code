tmp=map(int,raw_input().split())
n,m=tmp[0],tmp[1]
ad=
for _ in range (m):
    tmp=map(int,raw_input().split())
    fs,ls,fl=tmp[0],tmp[1],tmp[2]
    for i in range (fs,ls+1):
        ad=ad+fl
print ad/n