import numpy as np
import matplotlib.pyplot as plt


def animate(a, b, dt: float):
    plt.ion()
    fig, ax = plt.subplots()

    X = max(a.position[0], b.position[0]) * 1.5
    Y = max(a.position[1], b.position[1]) * 1.5
    ax.set(xlim=(-X, X), ylim=(-Y, Y))
    ax.set(xlabel="x", ylabel="y")

    a_location = ax.scatter([], [], s=80, color="crimson")
    b_location = ax.scatter([], [], s=80, color="royalblue")
    a_direction = ax.quiver(
        [], [], [], [], angles="xy", scale_units="xy", scale=1, color="crimson"
    )

    a_location.set_offsets(b.position)
    v = a.velocity / np.linalg.norm(a.velocity)
    a_direction.set_UVC(v[0], v[1])
    b_location.set_offsets(b.position)  # move marker instead of creating new figure
    fig.canvas.draw_idle()

    plt.pause(dt)
    plt.ioff()
    plt.show()
