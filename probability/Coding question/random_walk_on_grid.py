import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate a random walk on a 2D grid
def random_walk_2d(k):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions: up, right, down, left
    x, y = 0, 0  # Starting position (origin)
    walk = [(x, y)]  # List to store the path of the walk

    for _ in range(k):
        dx, dy = directions[np.random.choice(4)]  # Randomly choose one of the four directions
        x += dx  # Update the current position x
        y += dy  # Update the current position y
        walk.append((x, y))  # Append the new position to the walk

    walk.append((0, 0))  # Ensure the path returns to the origin at the end
    return walk

# Function to create a realistic animation of the random walk
def create_realistic_animation(walk):
    fig, ax = plt.subplots()
    
    def update(num):
        ax.clear()  # Clear the plot
        ax.set_aspect('equal')
        max_range = max(max(abs(x), abs(y)) for x, y in walk) + 1
        ax.set_xlim(-max_range, max_range)  # Set x-axis limits
        ax.set_ylim(-max_range, max_range)  # Set y-axis limits
        
        # Draw grid lines
        ax.set_xticks(np.arange(-max_range, max_range + 1))
        ax.set_yticks(np.arange(-max_range, max_range + 1))
        ax.grid(True)

        # Plot the path taken so far with a line
        path = np.array(walk[:num+1])
        ax.plot(path[:, 0], path[:, 1], 'b-', linewidth=2, label='Path')
        
        # Draw the person's current position as a larger red circle
        ax.plot(walk[num][0], walk[num][1], 'ro', markersize=10, label='Current Position')
        
        # Draw the starting position as a green square
        ax.plot(walk[0][0], walk[0][1], 'gs', markersize=10, label='Start Position')
        
        # Annotate the current position with step number
        ax.text(walk[num][0], walk[num][1], str(num), fontsize=12, ha='center', color='black')
        
        ax.set_title(f'Step {num}')
    
    ani = animation.FuncAnimation(fig, update, frames=len(walk), repeat=False)
    plt.gca().set_aspect('equal', adjustable='box')
    ax.legend(loc='upper left')  # Add the legend
    plt.show()

# Example usage
k = 50  # Number of steps
walk = random_walk_2d(k)  # Generate the random walk
create_realistic_animation(walk)  # Create and display the animation
