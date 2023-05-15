def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'A'

    result = 1
    result += explore_area(row-1, col, matrix)
    result += explore_area(row+1, col, matrix)
    result += explore_area(row, col-1, matrix)
    result += explore_area(row, col+1, matrix)

    return result


rows, cols = int(input()), int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if size == 0:
            continue
        areas.append((row, col, size))

print(f"Total areas found: {len(areas)}")
for index, area in enumerate(sorted(areas, key=lambda x: -x[-1])):
    print(f"Area #{index+1} at ({area[0]}, {area[1]}), size: {area[-1]}")