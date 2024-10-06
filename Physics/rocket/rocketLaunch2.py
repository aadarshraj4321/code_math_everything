import numpy as np
import matplotlib.pyplot as plt
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

# Create the figure and subplots
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 16))

# Initialize the subplots
def init():
    ax1.set_xlim(0, total_time)
    ax1.set_ylim(0, np.max(altitude) + 10)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Altitude (m)')
    ax1.set_title('Altitude vs. Time')

    ax2.set_xlim(0, total_time)
    ax2.set_ylim(0, np.max(fuel_remaining) + 10)
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Fuel Remaining (kg)')
    ax2.set_title('Fuel Remaining vs. Time')

    ax3.set_xlim(0, total_time)
    ax3.set_ylim(0, np.max(thrust) + 1000)
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Thrust (N)')
    ax3.set_title('Thrust vs. Time')

    ax4.set_xlim(-5, 5)
    ax4.set_ylim(0, np.max(altitude) + 10)
    ax4.set_xlabel('Horizontal Position (m)')
    ax4.set_ylabel('Altitude (m)')
    ax4.set_title('Rocket Launch Animation')

    return ax1, ax2, ax3, ax4

# Function to update the animation
def update(frame):
    # Clear previous lines
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    
    # Update altitude vs. time plot
    ax1.plot(time[:frame], altitude[:frame], color='b')
    ax1.set_xlim(0, total_time)
    ax1.set_ylim(0, np.max(altitude) + 10)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Altitude (m)')
    ax1.set_title('Altitude vs. Time')

    # Update fuel remaining vs. time plot
    ax2.plot(time[:frame], fuel_remaining[:frame], color='r')
    ax2.set_xlim(0, total_time)
    ax2.set_ylim(0, np.max(fuel_remaining) + 10)
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Fuel Remaining (kg)')
    ax2.set_title('Fuel Remaining vs. Time')

    # Update thrust vs. time plot
    ax3.plot(time[:frame], thrust[:frame], color='g')
    ax3.set_xlim(0, total_time)
    ax3.set_ylim(0, np.max(thrust) + 1000)
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Thrust (N)')
    ax3.set_title('Thrust vs. Time')

    # Update rocket launch animation with firing effect
    ax4.plot([0], [altitude[frame]], 'ro')
    ax4.plot([0, 0], [0, altitude[frame]], 'r--')
    ax4.set_xlim(-5, 5)
    ax4.set_ylim(0, np.max(altitude) + 10)
    ax4.set_xlabel('Horizontal Position (m)')
    ax4.set_ylabel('Altitude (m)')
    ax4.set_title('Rocket Launch Animation')

    # Add thrust visual effect
    if thrust[frame] > 0:
        ax4.plot([0], [altitude[frame] - 5], 'yo')
        ax4.plot([0, 0], [altitude[frame] - 5, altitude[frame] - 10], 'y--')

    return ax1, ax2, ax3, ax4

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=False)

# Show the animation
plt.tight_layout()
plt.show()
