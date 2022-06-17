x = int(input())
line = 0
end_index = 0

while x > end_index :
    line += 1
    end_index += line

diff = end_index - x

if line % 2 == 0 :
    top = int(line - diff)
    bottom = int(diff + 1)
else :
    top = int(diff + 1)
    bottom = int(line - diff)

print("%d/%d" %(top, bottom))

"""
우선 규칙을 찾아야 한다.
1줄 1개, 2줄 2개, 3줄 3개, 4줄 4개, 5줄 5개...
짝수라인은 분자가 점점 커지고, 분모가 점점 작아진다.
홀수라인은 분자가 점점 작아지고, 분모가 점점 커진다.
while문을 사용해서 끝의 인덱스값을 구하고 끝의 인덱스 값보다 입력값이
크면 멈추게 한다.
diff : 끝의 인덱스 값에서 입력값을 빼서 차이를 구해준다.
ex) x = 6, line = 3, end_index = 6, diff = 0
해당라인은 홀수라인이므로 끝 인덱스는 분자가 제일 작고 분모는 제일크다
top = diff + 1
bottom = line - diff 를 사용하면 해당 규칙을 나타낼 수 있다.

조금 더 규칙을 찾아보도록 노력하자
"""