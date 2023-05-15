def loop(num, arr, index):
    if index >= len(arr):
        print(' '.join([str(el) for el in arr]))
        return
    for n in range(1, num+1):
        arr[index] = n
        loop(num, arr, index+1)


number = int(input())
array = [None] * number
loop(number, array, 0)