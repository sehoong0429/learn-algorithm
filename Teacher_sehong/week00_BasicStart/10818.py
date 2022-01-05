## n개의 정수, 최솟값과 최댓값 구하기
n = int(input()) ##n개의 정수
n_list = list(map(int,input().split())) ##list 안에 숫자 값을 받기
nlist = sorted(n_list) ##입력 받은 값 정렬 n_list.sort() 라고 해도 됨.
print(nlist[0], nlist[-1]) ## 최솟값인 인덱스 0번째와 , 입력 받은 n개의 정수 - 1 을 하면 최댓값이 나온다.
## -1 을 하면 맨 끝으로 , -2 맨 끝에서 2번째 -> 유용하게 사용 가능 !