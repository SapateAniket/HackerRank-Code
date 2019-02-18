beautiful_cnt=
arr=raw_input().split()
mn, mx, k = int(arr[0]), int(arr[1]), int(arr[2])
for i in range(mn,mx,1):
    if (i - int((str(i))[::-1]) ) % k == 0 :
        beautiful_cnt = beautiful_cnt + 
print beautiful_cnt    