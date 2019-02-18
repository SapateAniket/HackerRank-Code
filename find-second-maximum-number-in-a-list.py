t=input()
y=[]
x=map(int,raw_input().split())
z=max(x)
for i in range(t):
    if x[i]!=z:
        y.append(x[i])
print max(y)
    
    
    