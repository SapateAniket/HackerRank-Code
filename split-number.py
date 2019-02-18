for _ in range(input()):
    st=raw_input()
    if '-' in st:
        l=st.split('-')
    else:
        l=st.split()
    print "CountryCode=%s,LocalAreaCode=%s,Number=%s" %(l[0],l[1],l[2])
