import numpy as np
import matplotlib.pyplot as plt

# Material constants
materials = {
    "Air": {"rho": 1.225, "Cd": 0.3},
    "Foam": {"rho": 60, "Cd": 0.9},
    "Sand": {"rho": 1770, "Cd": 2.62},
    "Water": {"rho": 1000, "Cd": 0.88},
}

# Common parameters
A = 0.0001344  # Projected area (m²)
m = 0.005  # Mass (kg)
v0 = 1700  # Initial velocity (m/s)
t = np.linspace(0, 0.001, 200)  # Time values

# Initialize figures
plt.figure(figsize=(10, 8))
plt.suptitle("Projectile Dynamics with Different Materials", fontsize=16)

# Velocity vs Time Plot
plt.subplot(2, 1, 1)
for material, props in materials.items():
    rho = props["rho"]
    Cd = props["Cd"]
    k = (rho * Cd * A) / (2 * m)  # Drag constant
    v_t = v0 / (1 + v0 * k * t)  # Velocity vs time
    plt.plot(t, v_t, label=f"{material}")
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.grid(True)

# Velocity vs Distance Plot
plt.subplot(2, 1, 2)
for material, props in materials.items():
    rho = props["rho"]
    Cd = props["Cd"]
    k = (rho * Cd * A) / (2 * m)  # Drag constant
    x = (1 / k) * np.log(1 + v0 * k * t)  # Distance vs time
    v_x = v0 * np.exp(-k * x)  # Velocity vs distance
    plt.plot(x, v_x, label=f"{material}")
plt.title("Velocity vs Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.xlim(0, 0.1)
plt.grid(True)

# Save the plots
output_file = "projectile_dynamics_materials.png"
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit the title
plt.savefig(output_file, dpi=300)
plt.close()
print(f"Combined plot saved as {output_file}")
