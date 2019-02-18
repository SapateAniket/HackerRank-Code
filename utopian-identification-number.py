import re
for _ in range(input()):
    t=raw_input()
    pat="[a-z]{3}[0-9]{2,8}[A-Z]{3}[A-Z]*"
    if re.match(pat,t):
        print "VALID"
    else:
        print "INVALID"
    