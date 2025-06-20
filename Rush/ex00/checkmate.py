def is_in_check(board):
    # First, we need to find the position of the King (denoted by 'K').
    king_position = None
    n = len(board)  # The size of the board (assuming a square board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break
    
    if not king_position:
        # If we didn't find the King, return an error message.
        return "Error: King not found"

    kx, ky = king_position

    # Directions for Rook and Queen (horizontal and vertical)
    rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Directions for Bishop and Queen (diagonal)
    bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Directions for Pawn (attacks diagonally)
    pawn_directions = [(-1, -1), (-1, 1)]  # Attacking directions for White pawn
    
    # Check for attacks from Rooks and Queens (vertical and horizontal)
    for dx, dy in rook_directions:
        x, y = kx + dx, ky + dy
        while 0 <= x < n and 0 <= y < n:
            if board[x][y] != '.':  # If we hidef checkmate(board: str):
    board = board.strip().split('\n')
    size = len(board)

    for row in board:
        if len(row) != size:
            print("Error")
            return

    king_pos = None
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")
        return

    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < len(board[x])

    def is_pawn_attacking():
        x, y = king_pos
        for dx, dy in [(-1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and board[nx][ny] == 'P':
                return True
        return False

    def is_bishop_attacking():
        x, y = king_pos
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece == 'B' or piece == 'Q':
                    return True
                else:
                    break
        return False

    def is_rook_attacking():
        x, y = king_pos
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece == 'R' or piece == 'Q':
                    return True
                else:
                    break
        return False

    if is_pawn_attacking() or is_bishop_attacking() or is_rook_attacking():
        print("Success")
    else:
        print("Fail")