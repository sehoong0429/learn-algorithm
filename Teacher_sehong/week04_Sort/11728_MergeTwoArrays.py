##정렬 되어 있는 배열을 합치고 정렬해서 출력하기

##a,b 각 배열의 크기를 입력 받는다.
N,M = map(int, input().split())


a = list(map(int, input().split()))
b = list(map(int, input().split()))

##extend (a 리스트의 끝에 b가 추가 되는 것)
a.extend(b)

##a.sort : 본체 리스트를 정렬해서 변환
##sorted(리스트) : 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환
print(*sorted(a))