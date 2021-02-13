inpt = input()
Tcounter = 0
Ccounter = 0
Gcounter = 0

for i in inpt:
    if i == 'T':
        Tcounter += 1
    elif i == 'C':
        Ccounter += 1
    elif i == 'G':
        Gcounter += 1
extra = min(Tcounter,Ccounter,Gcounter)

score = pow(Tcounter,2) + pow(Ccounter,2) + pow(Gcounter,2) + 7*extra
print(score)
