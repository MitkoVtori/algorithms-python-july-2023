def eight_queens(board):
    rows, cols, left_diagonal, right_diagonal = set(), set(), set(), set()

    def print_solution():
        for row in board:
            print(' '.join(row))
        print()

    def can_place_queen(r, c):
        if r in rows or c in cols or (r - c) in left_diagonal or (r + c) in right_diagonal:
            return False
        return True

    def set_queen(r, c):
        board[r][c] = '*'
        rows.add(r)
        cols.add(c)
        left_diagonal.add(r - c)
        right_diagonal.add(r + c)

    def remove_queen(r, c):
        board[r][c] = '-'
        rows.remove(r)
        cols.remove(c)
        left_diagonal.remove(r - c)
        right_diagonal.remove(r + c)

    def put_queens(row):
        if row == 8:
            print_solution()
            return
        for col in range(8):
            if can_place_queen(row, col):
                set_queen(row, col)
                put_queens(row + 1)
                remove_queen(row, col)

    put_queens(0)


chessboard = []
[chessboard.append(['-'] * 8) for _ in range(8)]

eight_queens(chessboard)