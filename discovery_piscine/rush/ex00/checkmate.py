def checkmate(board: str):

    # แปลง board เป็น list ของแถว
    rows = board.strip().splitlines()
    # print(rows)
    n = len(rows)

    # ต้องเป็นกระดานสี่เหลี่ยม
    for r in rows:
        if len(r) != n:
            return

    # หา King
    king_pos = None
    for i in range(n):
        for j in range(n):
            if rows[i][j] == 'K':
                king_pos = (i, j)

    if king_pos is None:
        return

    ki, kj = king_pos

    def ray_attack(di, dj, i, j):
        x, y = i + di, j + dj
        while 0 <= x < n and 0 <= y < n:
            if rows[x][y] != '.':
                return (x, y) == (ki, kj)
            x += di
            y += dj
        return False

    for i in range(n):
        for j in range(n):
            piece = rows[i][j]

            # Pawn
            if piece == 'P':
                if (i - 1, j - 1) == (ki, kj) or (i - 1, j + 1) == (ki, kj):
                    print("Success")
                    return

            # Bishop
            elif piece == 'B':
                for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if ray_attack(di, dj, i, j):
                        print("Success")
                        return

            # Rook
            elif piece == 'R':
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if ray_attack(di, dj, i, j):
                        print("Success")
                        return

            # Queen
            elif piece == 'Q':
                for di, dj in [
                    (-1, -1), (-1, 1), (1, -1), (1, 1),
                    (-1, 0), (1, 0), (0, -1), (0, 1)
                ]:
                    if ray_attack(di, dj, i, j):
                        print("Success")
                        return

    print("Fail")