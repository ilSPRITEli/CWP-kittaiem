import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    count = s.count('z')
    if count > 0:
        print("z" * count)
    else:
        print("none")
