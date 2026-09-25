PIECES = "KPBRQ"


def checkmate(rawboard):
    """
    rawboard รับ stringมา เปลี่ยนเป็น list of string
    """
    if not isinstance(rawboard, str):
        # rawboard.isStr()
        print("Error")
        return

    board = rawboard.splitlines()
    # board = ["R...", ".K..", "..P.", "...."]

    if not is_valid_board(board):
        print("Error")
        return

    king_pos = find_king(board)

    if (check_straight_lines(board, king_pos) or
            check_diagonal_lines(board, king_pos) or
            check_pawns(board, king_pos)):
        print("Success")
    else:
        print("Fail")


def is_valid_board(board):
    """
    กระดานต้องเป็นสี่เหลี่ยมจัตุรัส และมี King แค่ตัวเดียว
    """
    size = len(board)
    if size == 0:
        return False
    for line in board:
        if len(line) != size:
            return False
    king_count = sum(line.count('K') for line in board)
    return king_count == 1


def find_king(board):
    size = len(board)
    for x in range(size):
        for y in range(size):
            if board[x][y] == 'K':
                return (x, y)
    return None


def check_straight_lines(board, king_pos):
    """
    หาแนวตั้งแนวนอน นับจาก king (หา Rook, Queen)
    """
    # ขวา, ซ้าย, ล่าง, บน
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return check_directions(board, king_pos, directions, "RQ")


def check_diagonal_lines(board, king_pos):
    """
    หาแนวทแยงมุม นับจาก king (หา Bishop, Queen)
    """
    # ล่างขวา, ล่างซ้าย, บนขวา, บนซ้าย
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    return check_directions(board, king_pos, directions, "BQ")

                              #(1,1)
def check_directions(board, king_pos, directions, attackers):
    """
    เดินจาก king ไปแต่ละทิศ เจอตัวหมากตัวแรกแล้วหยุด
    ตัวอักษรที่ไม่ใช่ตัวหมาก ถือว่าเป็นช่องว่าง
    """
    size = len(board)
    k_x, k_y = king_pos

    for dx, dy in directions:
        # ยึดkingเป็นจุดเริ่มต้น เดินตามทิศไปเรื่อยๆ
        x, y = k_x + dx, k_y + dy

        while 0 <= x < size and 0 <= y < size:
            piece = board[x][y]
            if piece in attackers:
                return True
            if piece in PIECES: #< อันนี้คือถ้าเจอหมากที่ไม่ใช่ตัวที่เราต้องการหาก็หยุดเลย เพราะไม่ใช่ตัวแรกที่เจอแล้ว เช่น ถ้าเราหาแนวทะแทยง ตัวที่เป็นไปได้คือ Bishop กะ Queen ถ้าเจอตัวอื่นก็แปลว่าไม่ใช่ตัวแรกของทิศนั้นแล้ว
                break
            x += dx
            y += dy

    return False


def check_pawns(board, king_pos):
    """
    หาpawn นึกภาพ king จะโดน pawn กินได้มีแค่ซ้ายล่างกับขวาล่าง
    """
    size = len(board)
    k_x, k_y = king_pos
    to_check = [(1, -1), (1, 1)]

    for dx, dy in to_check:
        x = k_x + dx
        y = k_y + dy
        if 0 <= x < size and 0 <= y < size:
            if board[x][y] == 'P':
                return True
    return False
