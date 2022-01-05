N = int(input())


def factorial(number):
    if number == N:
        return N
    return number * factorial(number + 1)


if N == 0:
    print(1)
else:
    print(factorial(1))