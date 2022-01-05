##n이 주어졌을 때, n번째 피보나치 수를 구하기

##피보나치 공식 Fn = Fn-1 + Fn-2 (n>=2)
##피보나치 함수 만들기
def fibonacci(n):
    if n < 2 :
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input())
print(fibonacci(num))