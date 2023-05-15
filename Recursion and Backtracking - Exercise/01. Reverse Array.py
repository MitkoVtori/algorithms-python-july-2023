def reverse_array(arr, i=0):
    if i == 1:
        return ' '.join(arr)
    return reverse_array(arr[::-1], i=1)


array = input().split()
print(reverse_array(array))