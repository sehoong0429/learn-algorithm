##BreakEvenPoint
##a는 고정 비용
##b는 상품 만들 때 드는 비용
##c는 상품 가격

a, b, c = list(map(int, input().split()))

if b >= c: ##상품만들때 드는 비용이 상품보다 적으면 이익을 낼 수 없음
    print (-1)
else :
    print(a//(c-b)+1)
    ##+1 = 손익분기점을 만족하는 첫번째
    ##a가 100원 c-b가 10원이면 (a//c-b) = 1 , 1개를 팔았을때 본전 이기때문에 +1개를 더 팔아야 이익이 발생