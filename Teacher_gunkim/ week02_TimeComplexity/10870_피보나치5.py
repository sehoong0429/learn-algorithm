N = int(input())


def fibonacci(num):
    if num == 1 or num == 0:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(N))