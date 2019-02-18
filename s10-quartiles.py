# Enter your code here. Read input from STDIN. Print output to STDOUT
no = input()
arr = map(int, raw_input().split())
arr.sort()
q2 = arr[no/2]
print arr
med_pos = arr.index(q2)
print med_pos
if no % 2 == 1:
    q1 = ( arr[med_pos/2] + arr[med_pos/2 - 1]) / 
    q3 = ( arr[med_pos/2 + med_pos] + arr[med_pos/2 + med_pos + 1]) / 
else:
    q1 = arr[med_pos/2]
    q3 = arr[med_pos + med_pos/2]
    
print q1,q2,q