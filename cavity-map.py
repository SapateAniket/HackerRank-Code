for i in range (int(raw_input())):
    x=raw_input()
    j=
    for i in range(1,len(x)-1):
        y=x[i]
        j=i
        if x[i]>x[i-1] and x[i]>x[i+1]:
             break 
    print x[0:j-1]+"X"+x[j:len(x)]
        