a, b, c = list(map(int, input().split()))
if b >= c: # 판매 비용이 생산 비용보다 같거나 작으면 수익 낼 수 없음
    print(-1)
else:
    print((a // (c - b)) + 1)