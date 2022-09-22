#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
if __name__ == '__main__':
    for name in names:
        if name[:2] != '__':
            print(name)
