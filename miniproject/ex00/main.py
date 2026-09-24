from checkmate import checkmate

def main():
    board = """\
R...
.K..
.P..
....
\
"""
    result = checkmate(board)
    if result:
        print("Success")
    else:
        print("Fail")

if __name__ == "__main__":
    main()