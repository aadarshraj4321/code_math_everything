import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the array
arr = [10, 20, 30, 40, 50]

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, len(arr))
ax.set_ylim(0, max(arr) + 10)

# Create scatter plot to represent array elements
scat = ax.scatter(range(len(arr)), arr, c='blue', s=100)

# Initialize the plot limits
def init():
    scat.set_offsets(list(zip(range(len(arr)), arr)))
    return scat

# Animate the process of reversing the array
def animate(i):
    n = len(arr)
    if i < n // 2:
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    
    offsets = list(zip(range(len(arr)), arr))
    colors = ['blue'] * len(arr)
    
    if i < n // 2:
        colors[i] = 'red'
        colors[n - 1 - i] = 'red'
    
    scat.set_offsets(offsets)
    scat.set_color(colors)
    
    return scat

# Create an animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(arr)//2 + 1, interval=500, repeat=False)

# Display the animation
plt.show()
