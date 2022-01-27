import sys

T = int(input())
for i in range(T):
    parenthesis = list(sys.stdin.readline())[:-1] # 뒤에 '\n' 값이 하나 받아져서 slice한다.
    stack = []
    answer = 1
    for p in parenthesis:
        if p == '(': # '('는 추가
            stack.append(p)
        else: # ')'는 stack.top()이 '('일 때 짝이 됨. '('을 pop해준다.
            if len(stack) == 0 or stack[-1] != '(':
                answer = 0
                break
            else:
                stack.pop()

    if len(stack) == 0 and answer == 1:
        print('YES')
    else:
        print('NO')