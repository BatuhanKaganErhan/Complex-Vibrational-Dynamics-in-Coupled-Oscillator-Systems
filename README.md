# Complex Vibrational Dynamics in Coupled Oscillator Systems

## General Overview
This project models and analyzes the dynamics of coupled oscillators under varying boundary conditions (semi-fixed or free ends) using numerical integration. It provides detailed visualizations of the system's behavior across different oscillator configurations, contributing to computational physics studies and wave dynamics research.

## Features
- Simulates coupled oscillators with varying spring constants and masses.
- Supports boundary conditions like fixed-end and free-end.
- Visualizes the behavior of the oscillators, including energy distribution, velocity, and displacement.
- Provides detailed comparison of normal modes and wave dynamics for different oscillator configurations.

## Requirements
- Python 3.x or higher
- Required libraries:
  - numpy
  - matplotlib
  - scipy

## Running the Project
To run the project locally, follow these steps:

Clone the repository to your local machine:
`git clone https://github.com/BatuhanKaganErhan/Complex-Vibrational-Dynamics-in-Coupled-Oscillator-Systems.git`

Navigate to the project directory:
`cd Complex-Vibrational-Dynamics-in-Coupled-Oscillator-Systems`

Install the required dependencies:
`pip install numpy matplotlib scipy `

Run the script:
`python oscillator_dynamics.py`

The script will generate graphical outputs showing the behavior of the coupled oscillators over time.

## Functionality
The program defines the system of coupled harmonic oscillators using the function f_nosc. This function calculates the acceleration of each oscillator based on their positions and velocities. Specifically, it models the accelerations by considering the forces acting on each oscillator due to the springs connecting neighboring oscillators. The function solves the equations of motion for each oscillator in the system by incorporating the interactions with its neighboring oscillators. This allows the system to evolve over time based on the applied forces and initial conditions.

A list of oscillators, where each oscillator interacts with its neighboring ones via a spring force. The differential equations are numerically solved using scipy.integrate.solve_ivp, which integrates the equations of motion for the oscillators over a specified time range.


### Key Parameters
n: Number of oscillators in the system. The system can simulate various numbers of oscillators, such as 2, 4, 8, 12, etc.

k: Spring constant that determines the strength of the interaction between neighboring oscillators. In the code, it is set to 1.

m: Mass of each oscillator. This is also set to 1 in the code.

fixed_end: A boolean parameter indicating the boundary condition:

True means the ends of the chain are fixed, i.e., the first and last oscillators do not move.

False means the ends are free, i.e., all oscillators can move. This parameter is defined in the function call and can be changed to adjust the boundary condition.

### Initial Conditions
The initial state of the system is set by the function yStart(n):

Positions: All oscillators start at rest (position 0), except for the last oscillator, which is displaced by 0.3 to initiate the motion. Similarly, if desired, the positions of other oscillators can be set individually, just like the first and last oscillators.

Velocities: The initial condition for velocities sets all oscillators to a stationary state. If desired, individual oscillator velocities can be customized, similar to how positions are defined for the first and last oscillators.

## Analysis of Dynamics in Oscillator Systems

### The Thermodynamic and Complexity Effects of Oscillator Count on Dynamic Systems

As the number of oscillators increases (under the condition that only the last oscillator has a non-zero initial displacement of the same value), the average velocities, energies, and displacements of the oscillators decrease. This can be compared to systems containing the same internal energy but different numbers of identical atoms. As the number of atoms increases, the temperature decreases; similarly, an increase in the number of oscillators causes the energy to distribute across a broader range.

The increase in the number of oscillators also leads to an increase in the number of normal modes. Since the motion is composed of the superposition of these modes, the system evolves into a progressively more complex state. Furthermore, the interactions between the oscillators resemble the vibrational motion of atoms in an environment where cohesive and similar forces are negligible. Like atoms, oscillators exchange energy, and this energy exchange governs the overall dynamics of the system.

As the number of oscillators grows, the standard deviation of the mechanical energies of the oscillators at any given moment approaches zero. Assuming the system does not interact with any external system, if the number of oscillators were to approach infinity, distinguishing one oscillator from another would become impossible. At this point, the system would reach its maximum entropy, and no time-dependent changes could be observed. This scenario represents a state analogous to the thermodynamic end of the universe.

### The Role of Boundary Conditions in Dynamic Systems: Free and Fixed Ends

In a fixed-end system, the oscillators at the ends remain stationary while the others oscillate. 
In a free-end system, all oscillators can move, resulting in a different dynamic behavior.

The fundamental difference between fixed-end and free-end oscillator systems lies in the momentum and velocity of their centers of mass. When the system is near its initial state, the velocities and momentum of the centers of mass in both oscillator systems are variable. However, over time, in the fixed-end oscillator system, the velocity and therefore the momentum will continuously change due to the fixed ends, and the system will only be able to perform translational motion within certain limits. In the free-end oscillator system, the changes in momentum and velocity approach zero over time because the system's total energy is converted into potential energy. As a result, the speeds of the springs relative to each other decrease, and their motion slows down over time because the energy in the system is more evenly distributed, and there is no net acceleration.
In the free-end oscillator system, when the fixed_end parameter is set to False and initial values are input, it can be observed in the graph that, apart from the general oscillatory motion, the oscillators exhibit a net translational motion at the same speed.

We can compare the behavior of a free-end oscillator system to the movement of a caterpillar. As the caterpillar moves, it behaves similarly to a free-end oscillator system with an initial velocity only at one of its ends. It transfers the energy produced in its rear section to its front, propelling its entire body forward. When compared to a free-end oscillator system, a key difference is the caterpillar's necessity to continuously produce energy due to friction. In the caterpillar's rear muscles, chemical energy is converted into mechanical energy. In a frictionless environment, this energy should spread to the front without loss, but due to friction, this energy must be transferred to the front through muscle contractions. The caterpillar produces the necessary energy for contraction through biochemical reactions in its muscle cells. During this process, a portion of the energy is converted into heat and lost, while the rest is converted into mechanical energy, enabling the contraction. This mechanical energy is the primary source of the forces that cause the muscle fibers to move toward each other, and it forms the basic mechanism of the caterpillar's movement.

### The Effect of Mass and Spring Constant on the Vibrational Dynamics of Coupled Oscillators

As the spring constant increases, the springs become stiffer and restrict movement. This limits the independent motion of the masses, integrating them more into the overall motion of the system. In a theoretical scenario where the spring constant approaches infinity, the springs would barely move, and no potential energy would be stored. In such a system, any external force would result in an immediate and direct acceleration, as the role of the springs would become negligible. This would cause the system to behave like a completely rigid structure.

Stiff springs transmit forces between masses more quickly. At a high spring constant, the motion of one mass is immediately transferred to the others, reducing the phase difference between them. This makes the masses more dependent on each other. This behavior arises because the energy in the springs is transmitted in the form of waves, and the speed of these waves depends on the medium. In this case, the spring can be considered as the medium. When relating the wave speed to the dynamics of motion on the spring, the fundamental formula used to determine the wave speed is as follows:

**Wave speed**:  
v = sqrt(T / μ)

Where:
- **v**: Wave speed,
- **T**: Spring tension,
- **μ**: Mass density (mass per unit length).

Additionally, mass density can be calculated as:
μ = m / L

Where:
- **m**: Mass of the spring,
- **L**: Length of the spring.

These formulas are used to understand the wave speed and the dynamics of the system.

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

