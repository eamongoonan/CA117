from sys import stdin

class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(
            self.x + other.x,
            self.y + other.y
        )

def count(grid):
    c = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "-":
                fill(grid, vec2(x, y))
                c += 1
    return c

def fill(grid, point):
    inc = [vec2(1, 0), vec2(0, 1), vec2(-1, 0), vec2(0, -1)]
    step = 1
    grid[point.y][point.x] = "0"
    to_check = [[point + p for p in inc], []]
    while to_check[0] or to_check[1]:
        for point in to_check[0]:
            if len(grid) <= point.y or len(grid[0]) <= point.x:
                continue
            elif point.x < 0 or point.y < 0:
                continue
            elif grid[point.y][point.x] == "-":
                grid[point.y][point.x] = str(step)
                for p in inc:
                    to_check[1].append(p + point)
        step += 1
        to_check[0].clear()
        to_check[0], to_check[1] = to_check[1], to_check[0]

if (__name__ == "__main__"):
    stdin.readline()
    grid = [list(line.strip()) for line in stdin]
    print(count(grid))
    print("\n".join(["".join(line) for line in grid]))
