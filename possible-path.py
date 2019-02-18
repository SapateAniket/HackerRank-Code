from fractions import gcd
for _ in range(input()):
    st=map(int,raw_input().split())
    a,b,c,d=st[0],st[1],st[2],st[3]
    if gcd(a,b)==gcd(c,d):
        print "YES"
    else:
        print "NO"