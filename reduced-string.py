import string
st = raw_input()
uniq = set(i for i in st)
for i in uniq:
    x = i*
    if x in st:
        st = string.replace(st, x, "")
#        print st
if len(st) == 0:
    print 'Empty String'
else:
    print st