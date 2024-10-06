import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim



moves = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]


def isValidKnightMoves(x, y, board):
    return 0 <= x < board and 0 <= y < board



def knightMove(startRow, startCol, kMoves, board):
    positions = [[(startRow, startCol)]]
    currentPos = [(startRow, startCol)]
    
    for _ in range(kMoves):
        nextPos = []
        for x, y in currentPos:
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if isValidKnightMoves(nx, dx, board):
                    nextPos.append((nx, ny))
        positions.append(nextPos)
        currentPos = nextPos
    return positions


def createAnimation(positions, kMoves, board):
    fig, ax = plt.subplots()

    def update(step):
        ax.clear()
        # Chessboard draw
        for x in range(board):
            for y in range(board):
                rect = plt.Rectangle((x, y), 1, 1, fill=True, color='gray' if (x+y) % 2 == 0 else 'white')
                ax.add_patch(rect)

        # Knight pos draw
        for pos in positions[step]:
            knight = plt.Circle((pos[1] + 0.5, pos[0] + 0.5), 0.3, color="blue")
            ax.add_patch(knight)

        ax.set_xlim(0, board)
        ax.set_ylim(0, board)
        ax.set_xticks(np.arange(board + 1))
        ax.set_yticks(np.arange(board + 1))
        ax.grid(True)
        ax.set_title(f"Step {step}")

    ani = anim.FuncAnimation(fig, update, frames=len(positions), repeat=True)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()


board = 8
kMoves = 4
startRow = 1
startCol = 4
pos = knightMove(startRow, startCol, kMoves, board)
#print(pos)
createAnimation(pos, kMoves, board)
