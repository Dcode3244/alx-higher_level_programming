#!/usr/bin/python3
import sys
args = len(sys.argv)
ans = 0
for i in range(args - 1):
    ans += int(sys.argv[i + 1])
if __name__ == '__main__':
    print("{:d}".format(ans))
