# def get_fibonacci(n):
#     if n <= 1:
#         return 1
#     return get_fibonacci(n-1) + get_fibonacci(n-2)
def get_fibonacci(n):
    first_element = 0
    last_element = 1
    result = 0
    for i in range(n):
        result = first_element + last_element
        first_element, last_element = last_element, result
    return result


number = int(input())
print(get_fibonacci(number))