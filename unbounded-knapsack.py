for _ in range (int(raw_input())):
    x=map(int,raw_input().split())
    n,sum=x[0],x[1]
    y=map(int,raw_input().split())
    y.sort()
    tmp=
    flg=
    for j in range (n):
        if sum % y[j]==0:
            print sum
            break
        elif flg==0:
            flg=
            tmp=y[j]*(sum/y[j])
        elif tmp<y[j]*(sum/y[j]):
            tmp=y[j]*(sum/y[j])

        print tmp
            
            
            