# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=input()
shoe_size=map(int, raw_input().split(' '))
shoe_cntr=Counter(shoe_size)
earning = 
for i in range(input()):
    customer=map(int, raw_input().split(' '))
    if customer[0] in shoe_cntr.keys() and shoe_cntr[customer[0]] != 0:
        earning = earning + customer[1]
        shoe_cntr[customer[0]] = shoe_cntr[customer[0]] - 


print earning
