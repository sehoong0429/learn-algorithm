# 정수 1개를 입력받아 1 부터 입력받은 정수까지의 합 구하기
n = int(input())
r = 0
for i in range(1, n+1):
    r += i
print(r)