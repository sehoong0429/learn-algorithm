words = list(input().split())
dict = {}
duplicate = 0 # 중복 여부 체크
for word in words:
    if word not in dict: # 처음 보는 나오는 dict에 저장
        dict[word] = True
    else: # 아니라면 중복 문자
        duplicate = 1
        break
if duplicate == 1:
    print('no')
else:
    print('yes')