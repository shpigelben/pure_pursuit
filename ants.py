import numpy as np
import matplotlib.pyplot as plt
from pursuer_evador import Pursuer
import pursuit

if __name__ == "__main__":
    v0 = 1
    t = np.sqrt(3) / 2
    a = Pursuer(position=[-0.5, 0.0], velocity=[v0*0.1, v0*0.0])
    b = Pursuer(position=[0.5, 0.0], velocity=[-v0*0.1 * 0.5, v0*0.1 * t])
    c = Pursuer(position=[0.0, 3*t], velocity=[-v0*0.1 * 0.5, -v0*0.1 * t])

    dt = 0.05
    steps = 2000

    plt.ion()
    fig, ax = plt.subplots()
    ax.set(xlabel="x", ylabel="y")
    mu = (a.position + b.position + c.position) / 3
    L = 1
    ax.set(xlim=(mu[0] - L, mu[0] + L), ylim=(mu[1] - L, mu[1] + 2*L))

    a_location = ax.scatter([], [], s=40, color="crimson")
    b_location = ax.scatter([], [], s=40, color="royalblue")
    c_location = ax.scatter([], [], s=40, color="forestgreen")

    (a_trail_line,) = ax.plot([], [], linewidth=1, color="crimson")
    (b_trail_line,) = ax.plot([], [], linewidth=1, color="royalblue")
    (c_trail_line,) = ax.plot([], [], linewidth=1, color="forestgreen")

    a_trail_list = [[], []]
    b_trail_list = [[], []]
    c_trail_list = [[], []]

    for step in range(steps):
        a.update_velocity(b, 'pure_pursuit')
        b.update_velocity(c, 'pure_pursuit')
        c.update_velocity(a, 'pure_pursuit')

        a.move(dt)
        b.move(dt)
        c.move(dt)

        a_trail_list[0].append(a.position[0])
        a_trail_list[1].append(a.position[1])
        b_trail_list[0].append(b.position[0])
        b_trail_list[1].append(b.position[1])
        c_trail_list[0].append(c.position[0])
        c_trail_list[1].append(c.position[1])

        a_location.set_offsets(a.position)
        b_location.set_offsets(b.position)
        c_location.set_offsets(c.position)
        a_trail_line.set_data(a_trail_list[0], a_trail_list[1])
        b_trail_line.set_data(b_trail_list[0], b_trail_list[1])
        c_trail_line.set_data(c_trail_list[0], c_trail_list[1])

        fig.canvas.draw_idle()
        plt.pause(dt)

    plt.ioff()
    plt.show()
