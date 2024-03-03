def solution(n, m):
    answer = 0
    minn = min(n,m)
    gcd = 0
    lcm = 0

    for i in range(minn, 0, -1) :
        if n % i == 0 and m % i == 0 :
            gcd = i
            break
    lcm = (n*m) // gcd
    
    answer = [gcd, lcm]
    return answer

"""
최대공약수를 구하는 방법은 위와 같이 최소값을 구하고
최소값부터 0까지 역순으로 시작하여 n과 m을 i로 나누어서 처음에 나온 값으로 최대공약수를 구할 수 있다.
최소공배수를 구하는 방법은
(n*m) // gcd 를 통해 구할 수 있으니 해당 방법을 숙지하도록 하자.
"""