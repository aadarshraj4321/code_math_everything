import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Directions for moving right, down, left, and up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Function to check if a cell is within the maze bounds and is passable
def is_valid_move(maze, visited, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 1 and not visited[row][col]

# DFS function to find a path through the maze
def find_path_dfs(maze, row, col, path, visited):
    # Mark the current cell as visited
    visited[row][col] = True
    path.append((row, col))  # Add the current cell to the path for visualization

    # Base case: If the destination is reached, return True
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        return True

    # Explore all possible directions
    for d in directions:
        new_row, new_col = row + d[0], col + d[1]
        if is_valid_move(maze, visited, new_row, new_col):
            if find_path_dfs(maze, new_row, new_col, path, visited):
                return True

    # If no path is found, backtrack
    path.pop()
    return False

# Function to visualize the maze and the rat's exploration
def visualize_maze(maze, path):
    n, m = len(maze), len(maze[0])
    fig, ax = plt.subplots()
    ax.set_xlim(0, m)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')

    # Draw the maze
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                ax.add_patch(plt.Rectangle((j, n-i-1), 1, 1, color='white'))
            else:
                ax.add_patch(plt.Rectangle((j, n-i-1), 1, 1, color='black'))

    # Draw the path of the rat
    def update(frame):
        ax.clear()
        ax.set_xlim(0, m)
        ax.set_ylim(0, n)
        ax.set_aspect('equal')

        for i in range(n):
            for j in range(m):
                if maze[i][j] == 1:
                    ax.add_patch(plt.Rectangle((j, n-i-1), 1, 1, color='white'))
                else:
                    ax.add_patch(plt.Rectangle((j, n-i-1), 1, 1, color='black'))

        for r, c in path[:frame]:
            ax.add_patch(plt.Rectangle((c, n-r-1), 1, 1, color='blue'))

        if frame < len(path):
            r, c = path[frame]
            ax.add_patch(plt.Circle((c + 0.5, n-r-1 + 0.5), 0.3, color='red'))

    ani = FuncAnimation(fig, update, frames=len(path)+1, repeat=False, interval=300)
    plt.show()

# Main function to set up the maze, find the path, and visualize the exploration
def main():
    maze = [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1]
    ]

    path = []
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    if find_path_dfs(maze, 0, 0, path, visited):
        visualize_maze(maze, path)
    else:
        print("No path found")

# Run the main function
main()
