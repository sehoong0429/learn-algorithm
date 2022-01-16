##입력이 들어오는 순서대로 포켓몬 도감을 만들고, 번호가 들어오면 알맞은 포켓몬 이름을
##포켓몬 이름이 들어오면 알맞은 번호를 출력하는 문제
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}
##dict에 key: value로 번호:이름, 이름:번호로 한번씩 저장
for i in range(1, n + 1):
    name = input().rstrip()
    dict[i] = name
    dict[name] = i

# 포켓몬 탐색
for i in range(m):
    item = input().rstrip()
    if item.isdigit():
        print(dict[int(item)])
    else:
        print(dict[item])
