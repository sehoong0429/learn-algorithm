# 정수 2개를 각각 입력 받아서 몇 사분면에 위치하는지 출력하기
a = int(input())
b = int(input())
if a > 0 and b > 0 :
    print("1")
elif a < 0 and b > 0 :
    print("2")
elif a < 0 and b < 0 :
    print("3")
else:
    print("4")