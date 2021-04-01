a=["The Walking Dead","Entourage","The Sopranos","The Vampire Diaries"]
for i,show in enumerate(a):
    print(i)
    print(show)
    print(a[i])
for i in range(20,51):
    print(i)
b=["5","42","7","3","25","1","8","11","6"]
print(b)
while 1:
    a=input("Please a number or q: ")
    if a in b:
        print("Right")
    else:
        print("Wrong")
    if a=="q":
        break
c=[9,19,148,4]
d=[9,1,33,83]
e=[]
for i in c:
    for j in d:
        print(i,j,i*j)
        e.append(i*j)
print(e)
