word = input()
# 알파벳의 위치를 딕셔너리로 저장
dict = {}
for i in range(len(word)):
    if word[i] not in dict:
        dict[word[i]] = i
answer = []
# 알파벳 순서대로 answer 리스트에 위치 or -1 추가
start = 'a'
while start <= 'z':
    if start not in dict:
        answer.append(-1)
    else:
        answer.append(dict[start])
    start = chr(ord(start) + 1)
print(' '.join(map(str, answer)))