for _ in range (int(raw_input())):
    x=map(int,raw_input().split())
    a,b=x[0],x[1]
    flg=
    for i in range(b):
        if a==((i*i)%b):
            print "YES"
            flg=
            break
    if flg==0:
        print "NO"