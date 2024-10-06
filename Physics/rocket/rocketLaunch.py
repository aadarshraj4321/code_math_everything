import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Rocket parameters
rocket_mass = 1000  # kg
initial_fuel_mass = 500  # kg
thrust_force = 15000  # N
burn_rate = 5  # kg/s
gravity = 9.81  # m/s^2

# Simulation parameters
time_step = 0.1  # seconds
total_time = 60  # seconds
num_steps = int(total_time / time_step)

# Arrays to store simulation data
time = np.arange(0, total_time, time_step)
altitude = np.zeros(num_steps)
velocity = np.zeros(num_steps)
fuel_remaining = np.zeros(num_steps)
thrust = np.zeros(num_steps)

# Initial conditions
altitude[0] = 0.0
velocity[0] = 0.0
fuel_remaining[0] = initial_fuel_mass

# Simulation loop
for i in range(1, num_steps):
    if fuel_remaining[i-1] > 0:
        thrust[i] = thrust_force
        fuel_used = burn_rate * time_step
        fuel_remaining[i] = max(fuel_remaining[i-1] - fuel_used, 0)
    else:
        thrust[i] = 0
        fuel_remaining[i] = 0

    # Calculate acceleration
    acceleration = (thrust[i] - rocket_mass * gravity) / (rocket_mass + fuel_remaining[i])
    
    # Update velocity and altitude
    velocity[i] = velocity[i-1] + acceleration * time_step
    altitude[i] = altitude[i-1] + velocity[i] * time_step

# Initialize the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to initialize the plot
def init():
    ax.set_xlim(0, total_time)
    ax.set_ylim(0, np.max(altitude) + 10)
    ax.set_zlim(0, np.max(thrust) + 1000)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Altitude (m)')
    ax.set_zlabel('Thrust (N)')
    return ax

# Function to update the animation
def update(frame):
    ax.clear()
    init()
    ax.plot(time[:frame], altitude[:frame], thrust[:frame], color='b')
    ax.text(time[frame], altitude[frame], thrust[frame], f"Fuel: {fuel_remaining[frame]:.1f} kg", color='r')
    return ax

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=False)

# Show the animation
plt.title('Rocket Launch Simulation')
plt.show()
