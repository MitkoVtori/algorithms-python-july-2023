def paths_in_labyrinth(row, col, direction, lab, path):
    def inbound(l, r, c):
        try:
            if r < 0 or c < 0:
                return False
            return l[r][c]
        except IndexError:
            return False

    if not inbound(lab, row, col):
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
    elif lab[row][col] == '-':
        lab[row][col] = 'v'
        paths_in_labyrinth(row, col+1, 'R', lab, path)
        paths_in_labyrinth(row, col-1, 'L', lab, path)
        paths_in_labyrinth(row+1, col, 'D', lab, path)
        paths_in_labyrinth(row-1, col, 'U', lab, path)
        lab[row][col] = '-'

    path.pop()


rows, columns = int(input()), int(input())
lab = [[el for el in input()] for _ in range(rows)]
paths_in_labyrinth(0, 0, '', lab, [])