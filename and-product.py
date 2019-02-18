for I in range(int(raw_input())):
    a,b=map(int,raw_input().split())
    ans=a
    for J in range(a+1,b+1):
        ans=ans&J
    print ans    