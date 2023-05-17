numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    for j in range(1, len(numbers)-i):
        if numbers[j-1] > numbers[j]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j-1]

print(*numbers)