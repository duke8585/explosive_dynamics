import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # Ideal gas constant, J/(mol·K)
gamma = 1.4  # Adiabatic index
M_gas = 29e-3  # Molar mass of gas, kg/mol (TNT approximation)
T_initial = 300  # Initial temperature of the room, K
P_atm = 101325  # Atmospheric pressure, Pa

# Room and vent parameters
V_room = 50  # Room volume, m³
P_initial = 2 * P_atm  # Initial pressure in the room (2 bar)
A_vent = 0.5  # Vent area, m²
Cd = 0.7  # Discharge coefficient

# Time parameters
dt = 0.01  # Time step, seconds
time_end = 100  # Simulation duration, seconds
time_steps = int(time_end / dt)
times = np.linspace(0, time_end, time_steps)

# Initialize pressure array
P = np.zeros(time_steps)
P[0] = P_initial  # Set initial pressure

# Simulation loop
for t in range(1, time_steps):
    if P[t-1] > P_atm:
        # Calculate venting mass flow rate
        rho = P[t-1] / (R * T_initial / M_gas)  # Density of gas
        m_dot_vent = Cd * A_vent * np.sqrt(2 * rho * (P[t-1] - P_atm))
        
        # Update pressure (mass loss causes pressure drop)
        dm = -m_dot_vent * dt
        m = rho * V_room + dm  # Updated mass
        P[t] = m * R * T_initial / (M_gas * V_room)
    else:
        # Pressure cannot drop below atmospheric
        P[t] = P_atm

# Plot results
plt.figure(figsize=(10, 6), dpi=300)
plt.plot(times, P / 1e5, label="Pressure (bar)")
plt.axhline(P_atm / 1e5, color='r', linestyle='--', label="Atmospheric Pressure")
plt.title("Pressure Drop in a Room with Pressure Relief Vent")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (bar)")
plt.legend()
plt.grid()

# Save plot as high-resolution PNG
output_path = "pressure_drop_room.png"
plt.savefig(output_path, format='png', dpi=300)
# plt.show()

output_path