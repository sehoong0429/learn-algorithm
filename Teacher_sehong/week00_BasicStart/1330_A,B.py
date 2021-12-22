#정수 2개를 입력 받아서 크기 비교해서 맞는 부호 출력
a, b = map(int, input().split())
if a > b :
    print(">")
elif a < b :
    print("<")
else:
    print("==")
