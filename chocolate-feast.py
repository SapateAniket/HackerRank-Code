for i in range (int(raw_input())):
    tmp=map(int,raw_input().split())
    x,y,z=tmp[0],tmp[1],tmp[2]
    noc=x/y
    if noc<z:
        print noc
    else:
        wr=noc-noc/z
        noc+=(noc/z)+wr/z
        print noc