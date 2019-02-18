t=input()
st=list(raw_input())
inc=input()
for i in range(t):
    if st[i].isalpha() and st[i].isupper():
        fs,res=ord(st[i]),ord(st[i])+inc
        print chr(res)
        if res>ord('Z'):
            #print res
    
    
#print st
