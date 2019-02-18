t=input()
ar=[]
pr=[]
for _ in range(t):
    st=raw_input().split()
    ar.append(st[0])
    mrk=0    
    for i in range(1,4):
        mrk+=float(st[i])
    pr.append(mrk/3.0)
res=raw_input()
index=ar.index(res)
print "%.2f " %(pr[index])
    