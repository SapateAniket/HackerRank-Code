no = input()
key = map(float, raw_input().split())
value = map(int, raw_input().split())
#print key, value
arr = []
for i in range(no):
    for j in range(value[i]):
        arr.append(key[i])
arr.sort()
mid = len(arr) / 
if len(arr) % 2 == 0 :
    ar1 = arr[:mid]
    ar2 = arr[mid:]
    submid = len(ar1)/
    q1 = (ar1[submid] + ar1[submid-1] )/ 
    q3 = (ar2[submid] + ar2[submid-1] )/ 

    ar1 = arr[:mid]
    ar2 = arr[mid+1:]
    submid = len(ar1)/
    q1 = (ar1[submid] + ar1[submid-1] )/ 
    q3 = (ar2[submid] + ar2[submid-1] )/ 
    
print q3 - q
    