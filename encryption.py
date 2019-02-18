import math
st=raw_input()
le=len(st)
rows=int(math.floor(math.sqrt(le)))
cols=int(math.ceil(float(le)/rows))
if cols-rows==2:    
    cols-=
    rows+=
#print rows,cols
x,s,y,ls=0,"",0,[]
for i in range(cols):
    s=""
    x=y
    for j in range(rows):
        if x<=len(st)-1:
            s+=st[x]

    y+=
    ls.append(s)
print " ".join(ls)