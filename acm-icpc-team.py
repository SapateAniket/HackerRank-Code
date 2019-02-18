ar=map(int,raw_input().split())
p,t=ar[0],ar[1]
ls=[]
for i in range(p):
    x=input()
    ls.append(x)
mx,cnt=0,
for i in range(0,p):
    for j in range(i+1,p):
        x=str(ls[i]+ls[j])
        #print i,j,x
        if x.count('0')<mx:
            mx=x.count('0')
            cnt=
        if x.count('0')==mx:
            cnt+=1      

print cnt
