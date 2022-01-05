##세 개의 자연수 a, b, c 입력 받고 a * b * c 를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번 쓰였는지 출력

##abc 입력 받는다
a = int(input())
b = int(input())
c = int(input())

total = a * b * c ##total
result = [0] * 10 ##0부터 9까지 ( 10 크기의 리스트 , 개수를 담는 공간 - 숫자들이 몇번 쓰였는지 저장 )

##10진수에서 자리수 하나씩 체크 10으로 나누기
while total != 0: ##0이 되기 전까지
    result[total % 10] += 1 ##10으로 나누고 1증가시키고 result에 저장
    total //= 10 ##total 을 10으로 나누기 total = total // 10

##0번째 부터 출력
for item in result:
    print(item)