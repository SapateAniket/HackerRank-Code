for i in range(input()):
    arr=map(int,raw_input().split())
    n,k=arr[0],arr[1]
    ar=[i for i in range(n)]
    for i in range(len(ar)):
        ls=ar[i:]
        ls.reverse()
        ar[i:]=ls
    print ar.index(k)
        
        
        
