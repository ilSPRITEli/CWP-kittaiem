import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    tobesearched = sys.argv[2]
    if keyword == "" or keyword not in tobesearched:
        print("none")
    else:
        matches = re.findall(keyword, tobesearched)
        print(len(matches))
