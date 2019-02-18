l=int(raw_input())
r=int(raw_input())
m=l^l
for i in range (l,r):
    for j in range (i,r):
        if((i^j)>m):
           m=i^j
print m