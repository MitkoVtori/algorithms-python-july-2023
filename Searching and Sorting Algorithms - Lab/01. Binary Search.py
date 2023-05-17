def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid_index = (left + right) // 2
        mid_element = numbers[mid_index]
        if mid_element == target:
            return mid_index
        elif mid_element < target:
            left = mid_index + 1
        else:
            right = mid_index - 1
    return -1


numbers = list(map(int, input().split()))
target = int(input())
print(binary_search(numbers, target))
