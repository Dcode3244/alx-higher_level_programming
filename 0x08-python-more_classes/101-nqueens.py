#!/usr/bin/python3
""" prints a solution for nqueens puzzle """


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not (sys.argv[1]).isnumeric():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


class Solution:
    """ a class for the solution of n queens puzzle """

    def solve(self, n: int):
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)

        final = []
        for sol in range(len(res)):
            final.append([])
        sol = i = c = 0
        for soln in res:
            i = c = 0
            for row in soln:
                for col in row:
                    if col == 'Q':
                        final[sol].append([i, c])
                        c = 0
                        break
                    c += 1
                i += 1
            sol += 1

        for i in final:
            print(i)

        return res


new = Solution().solve(n)
