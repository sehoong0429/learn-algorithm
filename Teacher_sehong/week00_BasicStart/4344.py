## 학생수와 각 학생 점수가 주어질 때 평균을 넘는 학생들의 비율을 구하는 문제
## 입력 받을 케이스 수 C와 케이스에서 입력 받을 학생의 수 N
## N명의 각 점수를 입력 받아 각 케이스마다 평균을 넘는 학생들의 비율을 소수점 셋째자리까지 출력

n = int(input()) ##테스트 케이스의 개수
for i in range(n): ## for문을 n만큼 반복하기
    score = list(map(int,input().split())) ##학생수를 다른 변수에 저장하지 않고 score[0] 값이 학생 수 임을 가지고 감
    avg = sum(score[1:])/score[0] ##평균을 일반 변수로 받음. sum함수를 이용해 score에 있는 1번째 값 부터 마지막 값까지 다 더하고 sco[0]의 값인 학생수만큼 나눠 주는 것
    count = 0 ##count를 0으로 초기화

    ##for문으로 score의 1번째 값부터 마지막 값까지를 반복하여 출력
    for j in score[1:]:
        if j > avg: ##평균보다 큰 값이 있을 때 count를 1씩 증가
            count += 1

    ##print와 round를 이용해 최종 값을 출력해 줄 수 있다.
    print("%.3f%%" %round(count/score[0]*100,3)) ##round함수 (round(반올림 할 값, 반올림 위치 지정))
