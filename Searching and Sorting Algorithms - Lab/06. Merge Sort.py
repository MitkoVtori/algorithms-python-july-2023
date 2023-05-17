def merge_sort(numbers):
    def merge_arrays(left, right):
        sorted_arr = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sorted_arr.append(left[left_index])
                left_index += 1
            else:
                sorted_arr.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            sorted_arr.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            sorted_arr.append(right[right_index])
            right_index += 1

        return sorted_arr

    if len(numbers) == 1:
        return numbers

    mid_index = len(numbers) // 2
    left = numbers[:mid_index]
    right = numbers[mid_index:]

    return merge_arrays(merge_sort(left), merge_sort(right))


numbers = list(map(int, input().split()))
print(*merge_sort(numbers))
