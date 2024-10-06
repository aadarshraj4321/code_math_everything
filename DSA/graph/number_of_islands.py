
grid = grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
rows, cols = len(grid), len(grid[0])
visitedArr = [[False for _ in range(cols)] for _ in range(rows)]


def dfs(directions, visitedArr, row, col):
    visitedArr[row][col] = True
    for dr, dc in directions:
        print(dr, dc)




def numberOfIslands(grid):
    if not grid:
        return 0

    # up, down, left, right
    
    rows, cols = len(grid), len(grid[0])
    visitedArr = [[False for _ in range(cols)] for _ in range(rows)]
    print(visitedArr)



numberOfIslands(grid)
