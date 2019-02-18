t=int(raw_input())
ar=[0 for i in range(t)]
for i in range(t):
    ar[i]=map(int,raw_input().split())
    ar[i].sort()
flg=
for i in range(t-1):
    if ar[i][t]>ar[i+1][0]:
        flg=
        break
if flg==1:
    print "NO"
else:
    print "YES"

