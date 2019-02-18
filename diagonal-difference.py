no=input()
i=
matr,sml,smr=[],0,
for _ in range(no):
    x=raw_input().split()
    matr.append(x)
for i in range(no):
    sml+=int(matr[i][i])
    smr+=int(matr[i][no-i-1])
if sml>smr:
    print sml-smr
else:
    print smr-sml