import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim



def boardInit(n):
    fig, ax = plt.subplots()
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect("equal")

    chessBoard = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if((i + j) % 2 == 0):
                ax.add_patch(plt.Rectangle((i, j), 1, 1, color = "cornsilk"))
            else:
                ax.add_patch(plt.Rectangle((i, j), 1, 1, color = "saddlebrown"))

    return fig, ax, chessBoard


def isSafeBoard(board, row, col, n):

    # check co
    for i in range(row):
        if(board[i][col] == 1):
            return False

    # check upper left diagonal
    i, j = row - 1, col - 1
    while(i >= 0 and j >= 0):
        if(board[i][j] == 1):
            return False
        i -= 1
        j -= 1

    # check upper right diagonal
    i, j = row - 1, col + 1
    while(i >= 0 and j < n):
        if(board[i][j] == 1):
            return False

        i -= 1
        j += 1

    return True




def updateBoard(ax, chessBoard, queens):
    ax.clear()
    ax.set_xlim(0, len(chessBoard))
    ax.set_ylim(0, len(chessBoard))
    ax.set_aspect("equal")

    for i in range(len(chessBoard)):
        for j in range(len(chessBoard)):
            if((i + j) % 2 == 0):
                ax.add_patch(plt.Rectangle((i, j), 1, 1, color="cornsilk"))
            else:
                ax.add_patch(plt.Rectangle((i, j), 1, 1, color="saddlebrown"))

    # queen draw on board
    for row, col, in queens:
        ax.text(col + 0.5, row + 0.5, "♕", fontsize = 30, ha = "center", va = "center")
        
    

def solveNQueen(board, row, n, queens, animation):

    if(row >= n):
        return True

    for col in range(n):
        if(isSafeBoard(board, row, col, n)):
            board[row][col] = 1
            queens.append((row, col))
            animation.append(list(queens))

            if(solveNQueen(board, row + 1, n, queens, animation)):
                return True

            # BackTrack
            board[row][col] = 0
            queens.pop()
            animation.append(list(queens))
        
    return False


def nQueenAnimation(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    queens = []
    animations = []

    solveNQueen(board, 0, n, queens, animations)
    fig, ax, chessBoard = boardInit(n)

    def update(frame):
        queensFrame = animations[frame]
        updateBoard(ax, chessBoard, queensFrame)
        ax.set_title(f"Frame {frame + 1} / {len(animations)}")


    ani = anim.FuncAnimation(fig, update, frames = len(animations), interval = 1200, repeat = True)
    plt.show()






nQueenAnimation(8)















