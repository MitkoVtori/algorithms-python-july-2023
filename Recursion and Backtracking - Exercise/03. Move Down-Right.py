def find_exit(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows-1 and col == cols-1:
        return 1

    result = 0
    result += find_exit(row+1, col, rows, cols)
    result += find_exit(row, col+1, rows, cols)
    return result


rows, cols = int(input()), int(input())
print(find_exit(0, 0, rows, cols))