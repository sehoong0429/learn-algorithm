C = int(input())
for i in range(C):
    score = list(map(int, input().split()))
    # 평균 구하기
    average = sum(score[1:]) / score[0]
    # 평균을 넘는 학생 수 구하기
    people = 0
    for j in range(1, score[0] + 1):
        if score[j] > average:
            people += 1
    # format 메서드를 이용한 소수점 3자리 까지 출력
    print("{:.3f}%".format(people / score[0] * 100))