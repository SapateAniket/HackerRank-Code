for i in range(int(raw_input())):
    no=int(raw_input())
    ar=map(int,raw_input().split(" "))
    ar.sort()
    sm=
    x=
    for j in range(no):
        if ar[j]>=0:
            sm+=ar[j]
        if ar[j]<=0 and ar[j+1]>=0:
            x=ar[j]
    print str(sm+x)+" "+str(sm)
        
        