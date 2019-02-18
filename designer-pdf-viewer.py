h = map(int, raw_input().split())
word = list(raw_input())
mx_hight=
for i in word:
    if h[ord(i)%97] > mx_hight:
        mx_hight=h[ord(i)%97]
        
print mx_hight * len(word)