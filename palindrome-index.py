for _ in range(int(raw_input())):
    st=raw_input()
    flg=
    for i in range(len(st)-1):
        if st[i]!=st[len(st)-i-1]:
            if st[i]==st[len(st)-i-2]:
                print (len(st)-i-1)
                flg=
                break
            if st[i+1]==st[len(st)-i-1]:
                print i
                flg=
                break
    if flg==0:
        print "-1"
    
