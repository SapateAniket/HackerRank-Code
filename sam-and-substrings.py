# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_inter_cnt(s):
    ps = 
    for i in range(len(s)):
        ps = ps + int(''.join(s))
        s = s[:-1]
    return ps
    
    
no = list(raw_input())
sm, pos = 0, 
for i in range(len(no)):
    sm = sm + get_inter_cnt(no)
    no = no [1:]  
print sm    