import sys

N, M = map(int, sys.stdin.readline().split())
pocketmon = {} # 포켓몬 도감용 딕셔너리 생성
for i in range(N): # 도감에 이름-번호, 번호-이름 2개의 형태로 모두 저장한다
    name = sys.stdin.readline().split()
    pocketmon[str(i + 1)] = name[0]
    pocketmon[name[0]] = i + 1
for i in range(M): # 도감에서 찾아서 출력
    question = sys.stdin.readline().split()
    print(pocketmon[question[0]])