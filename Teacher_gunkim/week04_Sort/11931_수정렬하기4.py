import sys

N = int(input())
answer = []
for i in range(N):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for i in range(N):
    print(answer[N - i - 1])