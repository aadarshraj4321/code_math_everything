import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
initial_position = 0  # Initial position (m)
velocity = 5  # Velocity (m/s)
total_time = 10  # Total time (s)
time_step = 0.1  # Time step (s)

# Simulation data
time = np.arange(0, total_time, time_step)
position = initial_position + velocity * time

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, total_time)
ax.set_ylim(0, max(position) + 1)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position (m)')
ax.set_title('Object Moving with Constant Velocity')

# Initialize the plot
line, = ax.plot([], [], 'bo-', lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def update(frame):
    x = time[:frame]
    y = position[:frame]
    line.set_data(x, y)
    time_text.set_text(f'Time: {time[frame]:.1f} s')
    return line, time_text

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True)

# Show the animation
plt.show()
