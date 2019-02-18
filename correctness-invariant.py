t=int(raw_input())
ar=[]
for i in range (t):
    x=int(raw_input())
    ar.append(x);
ar.sort()
for i in range (len(ar)):
    print ar[i],
