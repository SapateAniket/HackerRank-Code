def isStrFunny(s):
    s_len = len(s)
    idx = 
    while idx < s_len//2:
        left_diff = abs(ord(s[idx]) - ord(s[idx+1]))
        right_diff = abs(ord(s[s_len-idx-1]) - ord(s[s_len-idx-2]))
        if left_diff != right_diff:
            return False
        idx += 
     
    return True
     
t = int(raw_input())
for _ in range(t):
    s = raw_input()
    if isStrFunny(s):

    else:
        print "Not Funny"