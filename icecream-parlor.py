for _ in range (int(raw_input())):
    sm=int(raw_input())
    tot=int(raw_input())
    ar=map(int,raw_input().split(" "))
    i,j=0,
    for i in range (tot):
        for j in range(i+1,tot):
            if ar[i]+ar[j]==sm:
                print i+1,j+
                break
            
            