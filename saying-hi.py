import re
for i in range(input()):
    s = raw_input().split()
    t=s[0].lower()
    #print t[:2]
    if t[:2]=='hi' :
        #print t
        if len(t)>2:
            #print t
            if(t[2]!='d'):
                print " ".join(s)
        else :
            tt=s[1]
            if (tt[0]!='d'):
                print " ".join(s)
                

    
    