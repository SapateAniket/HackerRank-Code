arr =map(int, raw_input().split())
no = map (int, raw_input().split())
arr1 = no[-arr[1]:]
arr1 += no[:-arr[1]]
for i in range(arr[2]):
    print arr1[input()]
    