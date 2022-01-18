#수 입력 받고, 중복되지 않게 정렬
##버블 정렬 - 이웃한 숫자를 비교하여 더 큰 수를 뒤로 보내는 방식
## n개의 숫자가 주어지면 n-1번 비교가 이루어지고 수의 배치와 상관없이 일정하게 탐색하기 때문에 o(n2)시간 복잡도를 가진다.

##입력 받을 수 의 개수 n
n = int(input())
list = []

##숫자 입력 받기
for i in range(n):
    list.append(int(input()))

##정렬
list.sort()

##하나씩 출력
for i in list:
    print(i)