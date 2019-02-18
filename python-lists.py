for _ in range(int(raw_input())):
    ls=[]
    x=raw_input().split();
    i,j=0,
    if x[0]=="insert":
        i,j=int(x[1]),int(x[2])
        ls.insert(i,j)
    
    if x[0]=="remove":
        i=int(x[1])
        ls.remove(i)
    if x[0]=="pop":
        ls.pop()
    if x[0]=="append":
        i=int(x[1])
        ls.pop(i)

        ls.sort()
    if x[0]=="reverse":
        ls.reverse(i)
    if x[0]=="print":
        print ls
        
        
        