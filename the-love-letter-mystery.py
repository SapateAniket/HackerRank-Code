t=int(raw_input())
x=[0 for i in range(t)]
cnt=
for i in range(t):
    y=raw_input()
    z=len(y)
    for j in range (z/2):
        if ord(y[j]) > ord(y[z-j-1]):
            cnt+= ord(y[j]) - ord(y[z-j-1])
        if ord(y[j]) < ord(y[z-j-1]):
            cnt+=  ord(y[z-j-1]) - ord(y[j])
    print cnt
    cnt=

    
