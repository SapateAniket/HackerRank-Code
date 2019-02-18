for _ in range(input()):
    t=map(int,raw_input().split())
    fs,ls,pos=t[0],t[1],t[2]
    nxt=
    for _ in range(1,pos):
            nxt=fs+ls
            fs=ls
            ls=nxt
    if pos==1:
        print ls
    elif pos==0:
        print fs
    else:
        print nxt   
            
        
