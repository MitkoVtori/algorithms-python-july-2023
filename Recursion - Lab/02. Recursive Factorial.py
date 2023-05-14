def get_factorial(n):
    if n == 0:
        return 1
    return n * get_factorial(n-1)


number = int(input())
print(get_factorial(number))