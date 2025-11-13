import numpy as np
import matplotlib.pyplot as plt
from pursuer_evador import Pursuer, Evader
import pure_pursuit
import animate

if __name__ == "__main__":

    a = Pursuer(position=[-1.0, -1.0], velocity=[ 1.0,  0.0])
    b = Pursuer(position=[ 1.0, -1.0], velocity=[ 0.0,  1.0])
    c = Pursuer(position=[ 1.0,  1.0], velocity=[-1.0,  0.0])
    d = Pursuer(position=[-1.0,  1.0], velocity=[ 0.0, -1.0])

    dt = 0.01
    steps = 2000

    plt.ion()
    fig, ax = plt.subplots(figsize = (8,8))
    ax.set(xlabel="x", ylabel="y")
    ax.set_aspect('equal')
    mu = (a.position + b.position + c.position + d.position) / 3
    L = 2
    ax.set(xlim=(mu[0] - L, mu[0] + L), ylim=(mu[1] - L, mu[1] + L))

    a_location = ax.scatter([], [], s=40, color="crimson")
    b_location = ax.scatter([], [], s=40, color="royalblue")
    c_location = ax.scatter([], [], s=40, color="forestgreen")
    d_location = ax.scatter([], [], s=40, color="orange")

    (a_trail_line,) = ax.plot([], [], linewidth=1, color="crimson")
    (b_trail_line,) = ax.plot([], [], linewidth=1, color="royalblue")
    (c_trail_line,) = ax.plot([], [], linewidth=1, color="forestgreen")
    (d_trail_line,) = ax.plot([], [], linewidth=1, color="orange")

    a_trail_list = [[], []]
    b_trail_list = [[], []]
    c_trail_list = [[], []]
    d_trail_list = [[], []]

    for step in range(steps):
        pure_pursuit.pure_pursuit(a, b)
        pure_pursuit.pure_pursuit(b, c)
        pure_pursuit.pure_pursuit(c, d)
        pure_pursuit.pure_pursuit(d, a)

        a.move(dt)
        b.move(dt)
        c.move(dt)
        d.move(dt)

        a_trail_list[0].append(a.position[0])
        a_trail_list[1].append(a.position[1])
        b_trail_list[0].append(b.position[0])
        b_trail_list[1].append(b.position[1])
        c_trail_list[0].append(c.position[0])
        c_trail_list[1].append(c.position[1])
        d_trail_list[0].append(d.position[0])
        d_trail_list[1].append(d.position[1])

        a_location.set_offsets(a.position)
        b_location.set_offsets(b.position)
        c_location.set_offsets(c.position)
        d_location.set_offsets(d.position)
        a_trail_line.set_data(a_trail_list[0], a_trail_list[1])
        b_trail_line.set_data(b_trail_list[0], b_trail_list[1])
        c_trail_line.set_data(c_trail_list[0], c_trail_list[1])
        d_trail_line.set_data(d_trail_list[0], d_trail_list[1]) 

        fig.canvas.draw_idle()
        plt.pause(dt)

    plt.ioff()
    plt.show()
