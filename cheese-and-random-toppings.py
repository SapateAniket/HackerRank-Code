import math
for _ in range(input()):
    arr=map(int,raw_input().split())
    a,b,t=arr[0],arr[1],arr[2]
    res=math.factorial(a)/(math.factorial(b)*math.factorial(a-b))
    print res%t