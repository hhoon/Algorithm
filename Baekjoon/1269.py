import sys
A, B = map(int, sys.stdin.readline().split())
li_A = set(map(int, sys.stdin.readline().split()))
li_B = set(map(int, sys.stdin.readline().split()))
difference = []

for i in li_A :
        if i not in li_B :
                difference.append(i)
for i in li_B :
        if i not in li_A :
                difference.append(i)
print(len(difference))