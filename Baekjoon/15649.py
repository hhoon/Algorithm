N, M = map(int, input().split())
li = []

def f():
	if len(li) == M :
		print(' '.join(map(str, li)))
		return

	for i in range(1, N+1) :
		if i in li:
			continue
		li.append(i)
		f()
		li.pop()
f()

"""
해당문제는 f()함수에서 for문을 돌렸을시
첫 예시의 3 1의 경우는
첫 for문에서 i가 1일때 1을 넣은 후 다시 f()로 들어가서 if문이 성립하기 때문에 print 하고 pop을 통해 해당 값을 지운다.
그 다음 i가 2일때도 위와 같이 반복하고, 3일때도 반복한 후 f()함수는 종료 된다.

두번째 예시인 4 2를 넣은 경우는
i가 1일때
1을 넣고 첫번째 f()함수에서 if문의 성립이 안되므로 다시 1을 넣는다. 그러고 다음 두번째f()에서 1을 넣어주면 길이가 2이기 때문에 3번째 f()에서는 출력해준다. 여기서 출력을 해줌으로써
3번째f()는끝나고 2번째 f()는  pop으로 넘어갈 수 있는듯하다. 그리고 pop에서 2번째 1을 제거해주고 2번째 f()는 2를 넣어주기를 반복한다.
그리고 if문을 통한 continue를 통해 중복을 방지해준다.

해설을 보고도 이해하는데 오래걸렸다. 함수를 많이 사용해보는 노력이 필요해보인다.
"""