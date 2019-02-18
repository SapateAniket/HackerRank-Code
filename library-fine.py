re=map(int,raw_input().split())
ex=map(int,raw_input().split())
if ex[2]!=re[2]:
    print "10000"
elif re[1]!=ex[1]:
    print 500*(re[1]-ex[1])
elif re[0]!=ex[0]:
    print 15*(re[0]-ex[0])
else:
    print '0'