t=raw_input().split(':')
#print t
if t[2].find("PM"):
    x=int(t[0])
    x+=1
    t[0],t[2]=x,t[2].replace("PM",'')
print str(t[0])+':'+t[1]+':'+t[2]