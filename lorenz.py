import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters for the Lorenz system
a = 10.0
b = 28.0
c = 8.0 / 3.0

# Define the differential equations
def f(state, t):
    x, y, z = state         # Unpack the state vector
    return a * (y - x), x * (b - z) - y, x * y - c * z 

# Initial state and time points
state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.01)

# Integrate the Lorenz equations
states = odeint(f, state0, t)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.plot(states[:, 0], states[:, 1], states[:, 2])
ax.view_init(elev = 20, azim = -60)

# Set axis limits to zoom in
ax.set_xlim([-19.9, 20]) 
ax.set_ylim([-20, 29])
ax.set_zlim([0, 49])   

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
