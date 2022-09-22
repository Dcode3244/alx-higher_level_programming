#!/usr/bin/python3
import sys
args = len(sys.argv) - 1
if __name__ == '__main__':
    if args == 1:
        print("{:d} argument:".format(args))
    else:
        print("{:d} arguments:".format(args))
    if args >= 1:
        for i in range(args):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
