import math

G = 6.67430e-11
M = 5.972e24
R = 6.371e6

def simulate_orbit(steps=1000, dt=10):
    x = R + 400e3
    y = 0

    vx = 0
    vy = 7670

    traj = []

    for _ in range(steps):

        r = math.sqrt(x**2 + y**2)

        ax = -G * M * x / r**3
        ay = -G * M * y / r**3

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

        traj.append((x, y))

    return traj