from math import pow
def f(n):return reduce(lambda x,y:x*y,range(1,n+1))
def s(x):
    print "%.3f"%(x -pow(x,3)/f(3) +pow(x,5)/f(5)-pow(x,7)/f(7)+pow(x,9)/f(9))
def c(x):
    print "%.3f"%(1-pow(x,2)/f(2)+pow(x,4)/f(4)-pow(x,6)/f(6)+pow(x,8)/f(8))
for _ in range(input()):
    x=float(raw_input())
    s(x)
    c(x)
    
    