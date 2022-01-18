##n개의 수가 주어졌을 때, 내림차순으로 정렬하기


import sys

n = int(input())
list =[]

for i in range(n):
    list.append(int(sys.stdin.readline()))
list.sort(reverse=True)

for i in list:
    print(i)