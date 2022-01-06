x, y = [], []
for _ in range(3): # x,y 좌표를 각각 입력받음
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
answer = []
for x1 in x: # 좌표의 값이 1개만 count 된다면 정답 좌표가 됨
    if x.count(x1) == 1:
        answer.append(x1)
for y1 in y:
    if y.count(y1) == 1:
        answer.append(y1)
print(' '.join(map(str, answer)))