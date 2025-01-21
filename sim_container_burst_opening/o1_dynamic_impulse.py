import math
import numpy as np
import matplotlib.pyplot as plt


def simulate_dynamic_pressure(
    V,  # Room volume (m^3)
    A_vent,  # Vent area (m^2)
    C_d,  # Discharge coefficient (dimensionless)
    P0,  # Ambient pressure (Pa)
    rho0,  # Ambient air density (kg/m^3)
    delta_mass,  # Total mass added by the explosion (kg)
    mass_add_time,  # Time over which the mass is added (s)
    duration=0.5,  # Total simulation time (s)
    dt=1e-6,  # Time step (s)
    R=287.05,  # Specific gas constant for air (J/kg.K)
    T=293.15,  # Temperature (K)
):
    """
    A simple dynamic simulation that gradually adds explosive mass over a given time period.
    As pressure increases, mass flows out of the vent. This allows the vent size to influence the peak pressure.

    Returns:
    times (list), pressures (list), peak_pressure (float)
    """

    # Initial conditions
    time = 0.0
    m_inside = (P0 * V) / (R * T)  # mass of air at ambient conditions
    peak_pressure = P0

    pressures = []
    times = []

    # Simulation loop
    while time < duration:
        # Calculate current pressure
        P_inside = (m_inside * R * T) / V
        if P_inside > peak_pressure:
            peak_pressure = P_inside

        # Add mass gradually if still within mass_add_time
        if time <= mass_add_time:
            # Fraction of mass to add this step
            mass_increment = (delta_mass / mass_add_time) * dt
            m_inside += mass_increment

        # Calculate outflow if inside pressure is greater than outside
        if P_inside > P0:
            rho_inside = m_inside / V
            pressure_diff = P_inside - P0
            m_dot_out = C_d * A_vent * math.sqrt(2 * rho_inside * pressure_diff)
        else:
            m_dot_out = 0.0

        # Update mass inside
        m_inside -= m_dot_out * dt
        if m_inside < 0:
            m_inside = 0.0

        pressures.append(P_inside)
        times.append(time)
        time += dt

    return np.array(times), np.array(pressures), peak_pressure


if __name__ == "__main__":
    # Define constant parameters
    V = 50.0  # Room volume in m^3
    P0 = 101325.0  # Ambient pressure in Pa
    rho0 = 1.225  # Ambient air density (kg/m^3)
    T = 293.15  # Temperature (K)
    R = 287.05  # Gas constant for air (J/kg.K)
    C_d = 0.7  # Discharge coefficient
    delta_mass = 100  # Total explosive mass in kg
    mass_add_time = 0.001  # Add mass over 2 ms
    duration = 0.1  # Total simulation time (s)
    dt = 1e-5

    # Series of vent areas to compare
    A_values = [0.01, 0.05, 0.1, 0.2, 1, 10]

    # Plot Pressure vs. Time
    plt.figure(figsize=(10, 6))
    for A_vent in A_values:
        times, pressures, peak_p = simulate_dynamic_pressure(
            V, A_vent, C_d, P0, rho0, delta_mass, mass_add_time, duration, dt, R, T
        )
        plt.plot(times, pressures, label=f"A_vent={A_vent} m²")
    plt.title("Pressure vs. Time for Different Vent Areas")
    plt.xlabel("Time (s)")
    plt.ylabel("Pressure (Pa)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("o1_pressure_vs_time.png", dpi=300)
    # plt.show()

    # Plot Cumulative Impulse (Integrated Pressure over Time)
    # Impulse per unit area = ∫ p(t) dt
    # We'll assume pressures are already in N/m² and dt in seconds, so the integral is straightforward.
    plt.figure(figsize=(10, 6))
    for A_vent in A_values:
        times, pressures, _ = simulate_dynamic_pressure(
            V, A_vent, C_d, P0, rho0, delta_mass, mass_add_time, duration, dt, R, T
        )
        # Integrate pressure over time to get cumulative impulse per unit area
        # Since dt is constant, we can do a cumulative sum:
        impulse = np.cumsum(pressures) * dt
        plt.plot(times, impulse, label=f"A_vent={A_vent} m²")

    plt.title("Cumulative Impulse vs. Time for Different Vent Areas")
    plt.xlabel("Time (s)")
    plt.ylabel("Impulse per unit area (N·s/m²)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("o1_impulse_vs_time.png", dpi=300)
    # plt.show()
