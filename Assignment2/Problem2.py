def is_lo_shu_square(square: list[list[int]]) -> bool:
    if len(square) != 3: return False
    for row in square:
        if len(row) != 3: return False
    for i in range(3):
        if square[i][0] + square[i][1] + square[i][2] != 15: return False
        if square[0][i] + square[1][i] + square[2][i] != 15: return False
    return True


if __name__ == '__main__':
    square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    print(is_lo_shu_square(square))
