# Aerodynamics of a Cow

A simple program to calculate and visualize the aerodynamic properties of a cow in different positions (standing vs lying down). 

## Assumptions and Constants

- **Cd_s**: Drag coefficient when standing (0.9)
- **Cd_l**: Drag coefficient when lying down (1.2)
- **A_s**: Frontal area when standing (1.5 m²)
- **A_l**: Frontal area when lying down (2.5 m²)
- **rho_sea**: Air density at sea level (1.225 kg/m³)
- **v**: Cow's velocity (10 m/s)
- **L**: Characteristic length of the cow (2.0 m)
- **mu**: Dynamic viscosity of air (1.81e-5 kg/(m·s))
- **g**: Gravity (9.81 m/s²)
- **m**: Cow's mass (600 kg)
- **Cl**: Lift coefficient (0.1, just for fun)

## What Does the Program Do?

1. **Drag Force**: Calculates the resistance force a cow faces when moving through the air.
2. **Lift Force**: (~~Not~~ Really Useful) Calculates the force that would lift the cow off the ground if it were an SU-57 jet.
3. **Reynolds Number**: Helps determine the type of airflow around the cow.
4. **Terminal Velocity**: Calculates the max speed the cow would reach if it were dropped from a height (totally not hypothetically, of course).

## Visuals

The program also plots the drag force against velocity, so you can what happens to the cow when it chugs readbull :)

## Conclusion

Basically this shows if a cow moves with (teevr gati) high speed then what'll happen..
