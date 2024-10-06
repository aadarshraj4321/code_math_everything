import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation

# Define the array and the number of positions to rotate
arr = [10, 20, 30, 40, 50]
positions = 2

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, len(arr))
ax.set_ylim(-2, 2)

# Create circles to represent array elements
circles = [plt.Circle((i, 0), 0.3, color='blue') for i in range(len(arr))]
for circle in circles:
    ax.add_patch(circle)

# Add text to represent array elements
texts = [ax.text(i, 0, str(arr[i]), color='white', ha='center', va='center', fontsize=12) for i in range(len(arr))]

# Add arrows to indicate movement
arrows = [ax.arrow(0, 0, 0, 0, head_width=0.1, head_length=0.1, fc='gray', ec='gray') for _ in range(len(arr))]

# Add text for step-by-step explanation
step_text = ax.text(0, 1.5, '', ha='center', fontsize=12, color='black')

# Initialize the plot limits
def init():
    for i, circle in enumerate(circles):
        circle.set_center((i, 0))
        texts[i].set_position((i, 0))
        texts[i].set_text(str(arr[i]))
    for arrow in arrows:
        arrow.remove()
    return circles + texts + [step_text]

# Animate the process of rotating the array
def animate(i):
    if i < len(arr):
        rotated_array = arr[i:] + arr[:i]
        for j, val in enumerate(rotated_array):
            circles[j].set_center((j, 0))
            texts[j].set_position((j, 0))
            texts[j].set_text(str(val))

        for arrow in arrows:
            arrow.remove()
        arrows.clear()

        for j in range(len(arr)):
            start = (j, 0)
            end = ((j + positions) % len(arr), -1)
            arrow = ax.arrow(start[0], start[1], end[0] - start[0], end[1] - start[1], head_width=0.1, head_length=0.1, fc='gray', ec='gray')
            arrows.append(arrow)

        step_text.set_text(f'Step {i + 1}: Rotate by {positions} positions')
    return circles + texts + arrows + [step_text]

# Create an animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(arr), interval=1000, repeat=False)

# Display the animation
plt.show()
