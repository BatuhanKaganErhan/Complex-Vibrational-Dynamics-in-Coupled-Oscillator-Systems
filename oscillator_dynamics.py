import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Function to define the differential equations of the coupled oscillators
def f_nosc(t, y, n, k, m, fixed_end):
    # Splitting the state vector into positions and velocities
    r = y[0:n]  # Positions of the oscillators
    v = y[n:2*n]  # Velocities of the oscillators
    eqs = []  # List to store the acceleration equations for each oscillator
    
    
    # If the ends are fixed (boundary condition)
    if fixed_end is True :
        for i in range(n):
            if i == 0:  # First oscillator
                eq = -k/m*(2*r[i] -r[i+1])  # Force considering neighbor
            elif i == n-1:  # Last oscillator
                eq = -k/m*(2*r[i] -r[i-1])  # Force considering only the previous neighbor
            else:  # Middle oscillators
                eq = -k/m*(2*r[i] -r[i-1] -r[i+1])  # Force from both neighbors
            eqs.append(eq)
    else :  # For free end conditions
        for i in range(n):  
            if i == 0:  # First oscillator
                eq = -k/m*(r[i] -r[i+1])  # Force considering neighbor
            elif i == n-1:  # Last oscillator
                eq = -k/m*(r[i] -r[i-1])  # Force considering only the previous neighbor
            else:  # Middle oscillators
                eq = -k/m*(2*r[i] -r[i-1] -r[i+1])  # Force from both neighbors
            eqs.append(eq)
    
    
    # Combine velocities and accelerations into a single list
    return list(v) + eqs


# Time range for the simulation
tStart = 0  # Start time
tEnd = 100  # End time


# List of oscillator counts to simulate
n_list = [2, 4, 8, 12, 15, 20, 25, 30]
k = 1  # Spring constant
m = 1  # Mass of each oscillator
fixed_end = True  # Whether the ends are fixed


# Function to define initial conditions
def yStart(n):
    
    positions = n*[0]  # Initial positions of all oscillators (all at rest initially)
    velocities = n*[0]  # Initial velocities of all oscillators (all stationary)
    
    positions[-1] = 0.3  # Set the initial displacement for the last oscillator
    positions[0] = 0  # Set the initial displacement for the first oscillator
    return positions + velocities  # Return combined positions and velocities



# List to store the solutions for different oscillator counts
solutions = []


# Solve the differential equations for each oscillator count
for i in range(len(n_list)):
    n = n_list[i]
    
    solution = solve_ivp(
        f_nosc,  # Function defining the ODEs  
        [tStart, tEnd],  # Time range for the solution  
        yStart(n),  # Initial conditions
        args=(n,k,m,fixed_end),  # Parameters for the ODE function
        method = 'RK45',  # Numerical integration method
        t_eval = np.linspace(0,100,1001)  # Times at which to evaluate the solution
    )
    
    solutions.append(solution)  # Store the solution
    
fig, axes = plt.subplots(4, 2, figsize=(10.5,12))  # Create subplots to visualize the results
    


# Plot the results for each oscillator count    
for i in range(len(n_list)):  
    n = n_list[i]  # Current number of oscillators
    k = 0   # Index to iterate through oscillators
    
    # Plot the position of each oscillator
    while k < n:
        axes.flat[i].plot(solutions[i].t, solutions[i].y[k] + (k+1))  # Offset each oscillator for clarity
        k = k+1            

i = 0   # Initialize the index for the first subplot

# Loop to add titles to each subplot
for n in n_list:  
    n = n_list[i]  # Get the current number of oscillators
    axes.flat[i].set_title(f'{n} oscillators')  # Set the title of the subplot to indicate the number of oscillators
    i = i + 1  # Increment the index to move to the next subplot

# Adjust layout for better visualization
plt.tight_layout()
