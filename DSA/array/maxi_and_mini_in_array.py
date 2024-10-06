import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define the array
arr = [10, 20, 30, 5, 40, 50]

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1, len(arr))
ax.set_ylim(0, max(arr) + 10)
ax.set_zlim(0, 10)

# Create scatter plot to represent array elements
scat = ax.scatter(range(len(arr)), arr, [0]*len(arr), c='blue', s=100)

# Initialize text for displaying min and max
text_min = ax.text2D(0.02, 0.95, '', transform=ax.transAxes, color='green', fontsize=12)
text_max = ax.text2D(0.02, 0.90, '', transform=ax.transAxes, color='red', fontsize=12)

# Initialize the plot limits
def init():
    scat._offsets3d = (range(len(arr)), arr, [0]*len(arr))
    text_min.set_text('')
    text_max.set_text('')
    return scat, text_min, text_max

# Animate the process of finding min and max
def animate(i):
    min_val = min(arr[:i+1])
    max_val = max(arr[:i+1])
    
    offsets = (range(len(arr)), arr, [0]*len(arr))
    colors = ['blue'] * len(arr)
    
    if i >= 1:
        min_index = arr.index(min_val)
        max_index = arr.index(max_val)
        colors[min_index] = 'green'
        colors[max_index] = 'red'
    
    scat._offsets3d = offsets
    scat.set_color(colors)
    
    text_min.set_text(f'Min: {min_val}')
    text_max.set_text(f'Max: {max_val}')
    
    return scat, text_min, text_max

# Create an animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(arr), interval=500, repeat=False)

# Display the animation
plt.show()
