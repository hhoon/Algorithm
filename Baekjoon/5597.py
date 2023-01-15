student = []
nohomework = []

for i in range(28) :
    student.append(int(input()))

for j in range(30) :
    try :
        student.index(j+1)
    except :
        nohomework.append(j+1)

nohomework.sort()
print(nohomework[0])
print(nohomework[1])