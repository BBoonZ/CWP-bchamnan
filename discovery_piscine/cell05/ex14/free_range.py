import sys

if sys.argv == 1:
    print("none")
else:
    print(list(range (int(sys.argv[1]), int(sys.argv[2]) + 1)))