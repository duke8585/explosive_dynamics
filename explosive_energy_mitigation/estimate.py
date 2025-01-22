import numpy as np
import matplotlib.pyplot as plt

# Constants
c_w = 4.18  # Specific heat capacity of water (kJ/kg·°C)
L_v = 2260  # Latent heat of vaporization (kJ/kg)
c_v = 2.01  # Specific heat capacity of vapor (kJ/kg·°C)
T_initial = 25  # Initial water temperature (°C)
T_boiling = 100  # Boiling point of water (°C)
TNT_energy_per_kg = 4184  # Energy of TNT per kg (kJ)

# Inputs
TNT_mass = 50  # Fixed amount of explosive in TNT equivalent (kg)
E_explosive = TNT_mass * TNT_energy_per_kg  # Total explosive energy (kJ)
water_masses = np.linspace(0, 100, 100)  # Water masses (kg)

# Energy absorbed by water
Q_water = (water_masses * c_w * (T_boiling - T_initial)) + (water_masses * L_v)

# Effective energy
E_effective = E_explosive - Q_water
E_effective[E_effective < 0] = 0  # Energy cannot be negative

# Mitigation efficiency
mitigation_efficiency = Q_water / E_explosive
mitigation_efficiency[mitigation_efficiency > 1] = 1  # Efficiency cannot exceed 100%

# Plot results
plt.figure(figsize=(12, 6))

# Effective energy plot
plt.subplot(1, 2, 1)
plt.plot(water_masses, E_effective, label="Effective Energy")
plt.axhline(y=0, color="r", linestyle="--", label="Zero Energy")
plt.xlabel("Water Mass (kg)")
plt.ylabel("Effective Energy (kJ)")
plt.title(f"Effective Energy vs. Water Mass\n(TNT Mass: {TNT_mass} kg)")
plt.legend()

# Mitigation efficiency plot
plt.subplot(1, 2, 2)
plt.plot(water_masses, mitigation_efficiency * 100, label="Mitigation Efficiency")
plt.xlabel("Water Mass (kg)")
plt.ylabel("Mitigation Efficiency (%)")
plt.title(f"Mitigation Efficiency vs. Water Mass\n(TNT Mass: {TNT_mass} kg)")
plt.legend()

plt.tight_layout()
plt.savefig("explosive_mitigation_plot.png")  # Save the figure as a PNG
