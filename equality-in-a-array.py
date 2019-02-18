x = input()
arr = map(int, raw_input('').split(' '))
print len(arr) - max(arr,key=arr.count)