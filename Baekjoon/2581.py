M = int(input())
N = int(input())
prime = []

for i in range(M,N+1) :
	if i == 1 :
		continue
	for j in range(2, int(i** (1/2))+1) :
		if i % j == 0 :
			break
	else :
		prime.append(i)

if not prime :
	print(-1)
else :
	print(sum(prime))
	print(min(prime))