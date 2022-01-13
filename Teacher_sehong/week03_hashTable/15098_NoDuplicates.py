## 같은 단어가 반복이 되면 no , 반복되지 않으면 yes

##1
string = input().split()
print(['no', 'yes'][len(string)==len({*string})])


##2
string = tuple(input().split())
dict = {} ##딕셔너리 생성
answer = True ## 단어가 반복 되는 경우 false, 반복되지 않는 경우 true를 저장하는 변수

for i in string: ##입력 받은 문장 반복문
    if i not in dict.keys(): ##같은 key값이 없으면 담음
        dict[i] = True
    else: ##key값이 있으면
        answer = False
        break

##answer에 따라서 yes no 출력
if answer == False :
    print('no')
else:
    print('yes')