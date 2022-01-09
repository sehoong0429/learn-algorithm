##직사각형의 경계선까지 가는 거리의 최솟값

x, y, w, h = list(map(int, input().split()))

print(min(x,y,w-x,h-y))
##min함수는 괄호안에 문자열, 리스트와 같은 반복 가능한 iterable 자료형을 입력하면 요소들 중 최솟값을 반환.