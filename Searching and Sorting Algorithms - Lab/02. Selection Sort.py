numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    min_index = i
    for current_index in range(i + 1, len(numbers)):
        if numbers[current_index] < numbers[min_index]:
            min_index = current_index
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(*numbers)

# def selection_sort(numbers, sorted_nums):
#     if not numbers:
#         return sorted_nums
#     min_element = min(numbers)
#     sorted_nums.append(min_element)
#     numbers.remove(min_element)
#     return selection_sort(numbers, sorted_nums)
#
#
# list_numbers = list(map(int, input().split()))
# print(*selection_sort(list_numbers, []))
