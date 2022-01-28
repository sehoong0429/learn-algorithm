import sys

N = int(input())
order = list(map(int, sys.stdin.readline().split()))
stack = []
count = 1 # 몇 번째 학생이 받을 차례인가
i = 0

# 문제의 핵심 -> 줄서기를 한 곳에서 순번인 친구는 간식을 받고 아닌 친구는 대기 줄로 간다.
# 이때 대기줄에서 순번인 친구가 맨 앞에 있다면 간식을 받으면 된다. 따라서 2중 while문이 필요로 한다.
while order and i < len(order): # dequeue를 이용하지 않으려고 이렇게 해봤다.
    if order[i] == count:
        count += 1
    else:
        stack.append(order[i])
    i += 1
    while stack:
        if stack[-1] == count:
            count += 1
            stack.pop()
            continue
        break
if len(stack):
    print('Sad')
else:
    print('Nice')

