x, y, w, h = map(int, input().split())
a = abs(x-w)
b = abs(y-h)

print(min(x, y, a, b))

"""
abs를 사용하면 절대값을 구할 수 있다.
"""