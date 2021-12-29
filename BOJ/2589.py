
sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]
check_col = [False] * 9
check_row = [False] * 9
check_square = [False]