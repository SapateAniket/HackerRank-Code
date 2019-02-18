import re
pattern="^[.|_][0-9]{1,*}[A-Za-z]{0,*}[_]{0,1}$"
print pattern
for i in range(input()):
    st=raw_input()
    if re.match(pattern,st):
        print "VALID"
    else:
        print "INVALID"