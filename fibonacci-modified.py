a,b,n=map(int,raw_input().split())  
list=[0,a,b]  
i=3;  
while(i<=n):  
    list.append(list[-1]**2+list[-2])  
    i+=1;  
print list[n]  