import math
no = input()
arr = map(int, raw_input().split())
mean = sum(arr)/no
x = 
for i in range(no):
    x = x + (arr[i] - mean)**2 

str_dev = math.sqrt(x/no)    
print str_dev