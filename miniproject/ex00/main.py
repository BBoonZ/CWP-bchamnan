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
    if result == "Success":
        print("Success")
    elif result == "Fail":
        print("Fail")
    elif result == "Error":
        print("Error")

if __name__ == "__main__":
    main()