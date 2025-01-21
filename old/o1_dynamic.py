import math
import matplotlib.pyplot as plt


def simulate_dynamic_pressure(
    V,  # Room volume (m^3)
    A_vent,  # Vent area (m^2)
    C_d,  # Discharge coefficient (dimensionless)
    P0,  # Ambient pressure (Pa)
    rho0,  # Ambient air density (kg/m^3)
    delta_mass,  # Total mass added by the explosion (kg)
    mass_add_time,  # Time over which the mass is added (s)
    duration=0.1,  # Total simulation time (s)
    dt=1e-5,  # Time step (s)
    R=287.05,  # Specific gas constant for air (J/kg.K)
    T=293.15,  # Temperature (K), assume constant
):
    """
    A simple dynamic simulation that gradually adds explosive mass over a given time period.
    As pressure increases, mass flows out of the vent. This allows the vent size to influence the peak pressure.

    Assumptions:
    - Ideal gas: P = (m * R * T) / V
    - Gradual addition of mass: at each step, a fraction of delta_mass is added until mass_add_time passes.
    - Once adding mass is complete, no more mass enters the room.
    - Simple orifice flow: m_dot_out = C_d * A_vent * sqrt(2 * rho_inside * (P_inside - P0)) if P_inside > P0.
    - Temperature is constant and equal to the initial value.
    - This is a simplified model for demonstration purposes only.
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
        P_inside = (
            m_inside * R * T
        ) / V  # FIXME can this be right?, nrt = pv and what about the mass of the explosive?
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

    return times, pressures, peak_pressure


if __name__ == "__main__":
    # Define constant parameters
    V = 50.0  # Room volume in m^3
    P0 = 101325.0  # Ambient pressure in Pa
    rho0 = 1.225  # Ambient air density (kg/m^3)
    T = 293.15  # Temperature (K)
    R = 287.05  # Gas constant for air (J/kg.K)
    C_d = 0.7  # Discharge coefficient
    delta_mass = 5  # Total explosive mass in kg
    mass_add_time = 0.0002  # Add mass over 2 ms
    duration = 0.5  # Total simulation time (s)
    dt = 1e-6

    # Series of vent areas to compare
    A_values = [0.01, 0.05, 0.1, 0.2, 0.5, 1.0]

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
    # plt.show()
    plt.savefig("pressure_vs_time_dynamic.png", format="png", dpi=300)
