t=input()
a,b = 0,
x=[]
x.append(a)
for i in range(t-1):
    a,b = b,a+b
    x.append(a*a*a)
print x
        