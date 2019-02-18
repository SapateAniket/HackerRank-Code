t=int(raw_input())
flg=
for i in range (t):
    str1=raw_input()
    str2=raw_input()
    lt=len(str1)
    for j in range (len(str1)):
        x=str1[j]
        if str2.find(x)==1:
            print "YES"
            flg=-
            break
    if flg==0:
        print "NO"
    flg=
        