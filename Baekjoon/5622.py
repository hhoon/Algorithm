number = input()

ABC = ['A', 'B', 'C']
DEF = ['D', 'E', 'F']
GHI = ['G', 'H', 'I']
JKL = ['J', 'K', 'L']
MNO = ['M', 'N', 'O']
PQRS = ['P', 'Q', 'R', 'S']
TUV = ['T', 'U', 'V']
WXYZ = ['W', 'X', 'Y', 'Z']
time = 0

for i in range(len(number)):
	if number[i] in ABC :
		time += 3
	elif number[i] in DEF :
		time += 4
	elif number[i] in GHI :
		time += 5
	elif number[i] in JKL :
		time += 6
	elif number[i] in MNO :
		time += 7
	elif number[i] in PQRS :
		time += 8
	elif number[i] in TUV :
		time += 9
	elif number[i] in WXYZ :
		time += 10

print(time)

"""
제출 당시 ' B'로 입력이 되어서 채점당시 계속 틀렸었다.
오타에 주의하자!
"""