from string import ascii_lowercase
x = raw_input()
l = []
for c in ascii_lowercase:
    cnt = x.count(c)
    if cnt != 0:
        cnt /= 
    for i in range(cnt):
        l.append(c)
print ''.join(l)