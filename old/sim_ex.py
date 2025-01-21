import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # Ideal gas constant, J/(mol·K)
gamma = 1.4  # Adiabatic index
M_gas = 29e-3  # Molar mass of gas, kg/mol (TNT approximation)
T_initial = 3000  # Initial temperature of explosive gases, K
T_room = 300  # Room temperature, K
P_atm = 101325  # Atmospheric pressure, Pa

# Room and explosion parameters
V_room = 5  # Room volume, m³
W_explosive = 1  # Explosive mass, kg
A_vent = 0.0005  # Vent area, m²
Cd = 0.7  # Discharge coefficient

# Gas yield approximation
gas_yield = 0.8  # Fraction of explosive converted to gas
mass_gas = W_explosive * gas_yield  # Total mass of gas, kg
n_gas = mass_gas / M_gas  # Total moles of gas

# Time parameters
dt = 0.00001  # Time step, seconds
time_end = 0.100  # Simulation duration, seconds
time_steps = int(time_end / dt)
times = np.linspace(0, time_end, time_steps)

# Initialize pressure and mass arrays
P = np.zeros(time_steps)
m = np.zeros(time_steps)

# Initial conditions
P[0] = (n_gas * R * T_initial) / V_room
m[0] = mass_gas

# Simulation loop
for t in range(1, time_steps):
    # Calculate venting mass flow rate
    rho = m[t-1] / V_room  # Density of gas
    if P[t-1] > P_atm:
        m_dot_vent = Cd * A_vent * np.sqrt(2 * rho * (P[t-1] - P_atm))
    else:
        m_dot_vent = 0
    
    # Update mass and pressure
    dm = -m_dot_vent * dt
    m[t] = m[t-1] + dm
    P[t] = (m[t] * R * T_initial) / V_room

# Plot results
plt.figure(figsize=(10, 6), dpi=300)
plt.plot(times, P / 1e5, label="Pressure (bar)")
plt.axhline(P_atm / 1e5, color='r', linestyle='--', label="Atmospheric Pressure")
plt.title("Pressure Evolution in a Room with Venting")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (bar)")
plt.legend()
plt.grid()

# Save plot as high-resolution PNG
output_path = "pressure_simulation_highres.png"
plt.savefig(output_path, format='png', dpi=300)
# plt.show()

output_path