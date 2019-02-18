tmp2=[]
z=[]
for _ in range(input()):
    tmp=[]
    x=raw_input()
    y=input()
    tmp2.append(y)
    tmp.append(x)
    tmp.append(y)
    z.append(tmp)
tmp2.sort()
t=tmp2[1]
tmp2=[]
for i in range(len(z)):
    for j in range(1):
        if t==z[i][1]:

tmp2.sort()
for i in range(len(tmp2)):
    print tmp2[i]
    