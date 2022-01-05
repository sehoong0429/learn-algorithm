##0보다 크거나 같은 정수 N이 주어진다. 이때 N!을 출력하기

##팩토리얼 함수 만들기
def factorial(N):
    if N <= 1:
        return 1
    return N * factorial(N-1)

##n=3이라면 n!은 3*2*1 = n*(n-1)*(n-2)

n = int(input()) ##n입력 받고
print(factorial(n))  ##만든 함수를 사용하여 n! 출력