# 정수3개 출력 받아서 출력 값을 한줄에 하나씩 출력
a, b, c =map(int,input().split())
print((a+b)%c, ((a%c)+(b%c))%c , (a*b)%c,((a%c)*(b%c))%c, sep='\n')

