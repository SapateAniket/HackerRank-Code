# Enter your code here. Read input from STDIN. Print output to STDOUT
no=input()
arr=map(int, raw_input().split())
tmp=arr
tmp.sort()
print float(sum(arr)/float(no))
print float((arr[no/2-1] + arr[no/2])/2.0)
tmp_set=set(tmp)
mx, pos = 1, 
if len(tmp_set)==no:
    print tmp[0]
else:
    for i in tmp_set:
        if tmp.count(i)>mx:
            mx = tmp.count(i)
            pos = tmp.index(i)

    print tmp[pos]            
