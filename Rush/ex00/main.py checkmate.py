#ต้องการรู้ว่าคิงโดนอิสไหม
# โดยที่ Pอิสได้ต่อเมื่ออยู่ข้างบน / B แนวทแยง / R หน้าหลังซ้ายขวา / Q รูปดอกจันทร์ 
def checkmate(board_str): #แบ่งข้อความเป้นบันทัดเหมือนตารางหมากรุก
    board = [list(row) for row in board_str.splitlines()]
    n = len(board)

    king_pos = None #หาตำแหน่งว่ามี เค อยู่ในตารางไหมเก็บตัวแปลไว้ใน คิงพอต 
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                king_pos = (r, c) #อา=แถว ซี=คอลั่ม
                break
        if king_pos:
            break
    if not king_pos: #ถ้าไม่เจอเคในตารางจะแสดงผลเฟล
        print("Fail")
        return

    kr, kc = king_pos 
    def inside(r, c):
        return 0 <= r < n and 0 <= c < n

    for dc in [-1, 1]:
        pr, pc = kr - 1, kc + dc 
        if inside(pr, pc) and board[pr][pc] == 'P':
            print("Success")
            return

    directions_bishop = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for dr, dc in directions_bishop:
        r, c = kr + dr, kc + dc
        while inside(r, c):
            if board[r][c] != '.':
                if board[r][c] == 'B' or board[r][c] == 'Q':
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc
    directions_rook = [(-1,0), (1,0), (0,-1), (0,1)]
    for dr, dc in directions_rook:
        r, c = kr + dr, kc + dc
        while inside(r, c):
            if board[r][c] != '.':
                if board[r][c] == 'R' or board[r][c] == 'Q':
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc
    print("Fail")

def main():
    board1 = """\
....
..R.
.K..
...."""
    checkmate(board1)

    board2 = """\
PP
.K"""
    checkmate(board2)

if __name__ == "__main__":
    main()