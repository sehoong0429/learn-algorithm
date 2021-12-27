## 두 정수 a 와 b를 입력 받은 다음 a+b 를 출력
## 0 0 이 나오면 break
while 1 :
    A,B = input().split()
    if A and B == '0' : break
    else:
        print(int(A)+int(B))