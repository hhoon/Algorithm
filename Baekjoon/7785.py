n = int(input())
log = set()

for i in range(n) :
    name, where = input().split()
    if where == "enter" :
        log.add(name)
    else :
        log.remove(name)

log = list(log)
log.sort()
log.reverse()
for i in log :
    print(i)