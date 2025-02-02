import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, solve_ivp

# Parameters for the Lorenz System
a = 10.0
b = 28.0
c = 8.0 / 3.0

# Define the differential equations
def lorenz(t, state, a, b, c):
    x, y, z = state           # Unpack the state vector

    dx = a * (y - x)
    dy = x * (b - z) - y
    dz = x * y - c * z
    return [dx, dy, dz]

# Initial state and time points
p = (a, b, c)                 # Parameters of the system
y0 = [1.0, 1.0, 1.0]
t_span = (0.0, 40.0)
t = np.arange(0.0, 40.0, 0.01)
#t = np.arange(0.0, 15.0, 0.01)

# Integrate the Lorenz equations
# First method
# Solve a system of ordinary differential equations using lsoda
# from the FORTRAN library odepack
result_odeint = odeint(lorenz, y0, t, p, tfirst = True)
# Second method
# Solve an initial value problem for a system of ordinary
# differential equations
result_solve_ivp = solve_ivp(lorenz, t_span, y0, args = p)

# Create a 3D plot
fig = plt.figure(figsize = (12,6))
ax = fig.add_subplot(1, 2, 1, projection = "3d")
ax.plot(result_odeint[:, 0],
        result_odeint[:, 1],
        result_odeint[:, 2])
ax.set_title("odeint")

ax = fig.add_subplot(1, 2, 2, projection = "3d")
ax.plot(result_solve_ivp.y[0, :],
        result_solve_ivp.y[1, :],
        result_solve_ivp.y[2, :])

ax.set_title("solve_ivp")

plt.show()
