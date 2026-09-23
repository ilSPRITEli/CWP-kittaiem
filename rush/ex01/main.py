import sys
from checkmate import checkmate


def read_board(filename):
    try:
        with open(filename, "r") as file:
            return file.read().rstrip("\n")
    except (OSError, UnicodeDecodeError):
        return None


def main():
    args = sys.argv[1:]

    if not args:
        print("ลืมพิมพ์ไฟล์นะค้าบ")
        return

    for filename in args:
        board = read_board(filename)
        if board is None:
            print("Error")
            continue
        checkmate(board)

main()
