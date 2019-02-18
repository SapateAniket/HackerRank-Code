n=input()
chk=[]
for _ in range(n):
    st=raw_input().split()
    for ch in st:
        chk.append(ch)
for _ in range (input()):
    cnt=
    x=raw_input()
    cnt+=chk.count(x)
    x=x[:len(x)-2]+"se"
    cnt+=chk.count(x)
    print cnt
