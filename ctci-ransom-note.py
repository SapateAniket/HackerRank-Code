def ransom_note(magazine, ransom):
    cnt = 
    for i in ransom:
        if i in magazine:
            cnt = cnt + 
    if cnt != len(ransom):
        return 'No'
    return 'Yes'
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
print ransom_note(magazine, ransom)
 
    
