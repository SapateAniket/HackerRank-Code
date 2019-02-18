import re
for i in range(int(raw_input())):
    s = raw_input()
    pattern = "^[A-Z]{5}[0-9]{4}[A-Z]$"
    if re.match(pattern,s):
        print 'YES'
    else:
        print 'NO' 