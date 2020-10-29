from sys import stdin

def cc(grid):
    return[
        "".join([grid[j][i] for j in range(len(grid))])
        for i in reversed(range(len(grid[0])))
    ]

def cw(grid):
    return[
        "".join([grid[j][i] for j in reversed(range(len(grid)))])
        for i in range(len(grid[0]))
    ]

if (__name__ == "__main__"):
    words = sorted(
        cc([line.strip() for line in stdin]),
        key=lambda a: a.lower(),
        reverse=True
    )
    print("\n".join(cw(words)))
