import sys

if len(sys.argv) == 1:
    print("none")
else:
    found = False
    for arg in sys.argv[1:]:
        if arg.endswith('ism'):
            continue
        print(arg + "ism")
        found = True
    if not found:
        print("none")
