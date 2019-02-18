# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(raw_input())
ar1=[]
for i in range (t):
    x=int(raw_input())
    y=4294967295-x
    ar1.append(y)
for i in range (len(ar1)):
    print ar1[i]
    
    
