alphabet = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia :
	alphabet = alphabet.replace(i, "*")

print(len(alphabet))

"""
replace 함수를 사용하여서 문자를 변환할 수 있다.
주의할점은 for i in croatia 로 범위를 지정해야하고
alphabet = alphabet.replace(i, "*") 처럼 기존 변수를 사용해야한다.
alphabet2 = alphabet.replace(i, "*") 를 하면 기존 변수는 변형이 되지 않음으로 다시 문자열이 원형으로 돌아감으로 주의해야한다.
"""