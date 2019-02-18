for _ in range(input()):
    arr=map(int,raw_input().split())
    a,b,x,res=arr[0],arr[1],arr[2],
    ex=pow(a,b)
    res=ex/x
    if ex-res*x>ex-(res+1)*x and b>0:
        print res*x
    elif ex-res*x<ex-(res+1)*x and b>0:
        print (res+1)*x
    else:
        print 