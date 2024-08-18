import math
import matplotlib.pyplot as plt

# Constants
Cd_s = 0.9  
Cd_l = 1.2  
A_s = 1.5   
A_l = 2.5   
rho_sea = 1.225  
v = 10  
L = 2.0  
mu = 1.81e-5  
g = 9.81  
m = 600  
Cl = 0.1 

def drag_force(Cd, A, rho, v):
    return 0.5 * Cd * A * rho * v**2

# Though it's more for planes than cows
def lift_force(Cl, A, rho, v):
    return 0.5 * Cl * A * rho * v**2   

def reynolds_number(v, L, rho, mu):
    return (rho * v * L) / mu

def terminal_velocity(Cd, A, rho, m, g):
    return math.sqrt((2 * m * g) / (rho * Cd * A))

# Drag force vs. velocity
def graph(Cd, A, rho, max_v=30):
    velocities = range(0, max_v + 1)
    drag_forces = [drag_force(Cd, A, rho, v) for v in velocities]

    plt.plot(velocities, drag_forces, label=f'Cd={Cd}, A={A} m^2')
    plt.title('Drag Force vs. Velocity')
    plt.xlabel('Velocity (m/s)')
    plt.ylabel('Drag Force (N)')
    plt.grid(True)
    plt.legend()
    plt.show()

# The Force is strong with you
drag_standing = drag_force(Cd_s, A_s, rho_sea, v)
drag_lying = drag_force(Cd_l, A_l, rho_sea, v)
Re_standing = reynolds_number(v, L, rho_sea, mu)
vt_standing = terminal_velocity(Cd_s, A_s, rho_sea, m, g)
lift_standing = lift_force(Cl, A_s, rho_sea, v)

print(f"Drag Force (Standing): {drag_standing:.2f} N")
print(f"Drag Force (Lying Down): {drag_lying:.2f} N")
print(f"Reynolds Number (Standing): {Re_standing:.2e}")
print(f"Terminal Velocity (Standing): {vt_standing:.2f} m/s")
print(f"Lift Force (Standing): {lift_standing:.2f} N (Works only cuz we have a holy cow)")

# The drag force vs. velocity for both scenarios
graph(Cd_s, A_s, rho_sea)
graph(Cd_l, A_l, rho_sea)
