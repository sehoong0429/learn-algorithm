N, M = map(int, input().split())
dict = {}
for i in range(N): # 듣도 못한 사람 명단을 dict에 추가
    name = input()
    dict[name] = True
answer = []
for i in range(M): # 보도 못한 사람명단이 dict에 있다면 answer 리스트에 추가
    name = input()
    if name in dict:
        answer.append(name)
print(len(answer))
answer.sort() # 명단을 사전순으로 정렬
for ans in answer:
    print(ans)