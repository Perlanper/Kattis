inpt = input()
inpt2 = []
for i in range(int(inpt)):
    inpt2.append(input().split())
for i in inpt2:
    a = int(i[0])
    b = int(i[1])
    c = int(i[2])
    if a + b == c:
        print("Possible")
    elif a-b == c or b-a == c:
        print("Possible")
    elif a*b == c:
        print("Possible")
    elif a/b == c or b/a == c:
        print("Possible")
    else:
        print("Impossible")