import sys

N = int(input())


def top(s):
    if len(s) == 0:
        return -1
    return s[-1]


def empty(s):
    if len(s) == 0:
        return 1
    return 0


def pop(s):
    if len(s) == 0:
        return -1
    return s.pop()


stack = []
for i in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'top':
        print(top(stack))
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(empty(stack))
    elif command[0] == 'pop':
        print(pop(stack))