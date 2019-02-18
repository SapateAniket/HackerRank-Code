import math
p,q=int(raw_input()),int(raw_input())
sm=
sqr=
for i in range(p,q):
    sqr=pow(i,2)
    x=len(str(sqr))
    st=str(sqr)
    y,z=int(str(st[0:x/2])),int(str(st[x/2:x]))
    sm=y+z
    if sm==i:
        print i

    