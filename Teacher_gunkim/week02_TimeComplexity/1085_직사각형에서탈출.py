x, y, w, h = map(int, input().split())
print(min(x, min(y, min(w - x, h - y)))) # 현재 위치에서 직사각형에 도달할 수 있는 최소 거리