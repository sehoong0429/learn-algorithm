##듣도보도 못한 사람 리스트, 보도 못한 사람 리스트에서 중복 원소를 찾아야함

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

#듣도 보도 못한 종류의 관계없이, 이름을 key값으로 가져가고,
#key가 처음 생기는 경우라면 1을 집어 넣어줌.
dic = {}
for i in range(n+m):  # O(n)
    name = input().strip()
    # dictionary에 key값이 처음 들어가는 경우
    if name not in dic: #0(1)
        dic[name] = 1
    # dictionary에 key값이 이미 들어가 만들어져 있는 상태에서 같은 key값이 들어왔으면
    else:
        dic[name] = dic[name]+1  # O(1)

answer = []
##value가 2인 모든 key값을 출력
for k, v in dic.items():  # O(n)
    if v == 2:
        answer.append(k)
print(len(answer))
print("\n".join(sorted(answer)))  # O(n)