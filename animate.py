import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
from simulation import Simulation

def Animate(agents, dt, steps):
    sim = Simulation(agents, dt)

    plt.ion()
    fig, ax = plt.subplots(figsize=(8,8))
    
    colors = [plt.get_cmap('tab10')(i) for i in range(len(agents))]
    mu, std = sim.initial_com()
    L = 10
    ax.set(xlim = (mu[0]-L, mu[0]+L), 
           ylim = (mu[1]-L, mu[1]+L))
    fig.gca().set_aspect('equal', adjustable='box')
    

    locations = [ax.scatter([], [], s=40, color = colors[i]) 
                for i in range(len(agents))]
    trail_lines = [ax.plot([], [], linewidth=1)[0] for _ in agents]
    trail_lists = [[[], []] for _ in agents]
    for _ in range(steps):
        sim.run()
        for i, agent in enumerate(agents):
            locations[i].set_offsets(agent.position)

            trail_lists[i][0].append(agent.position[0])
            trail_lists[i][1].append(agent.position[1])
            trail_lines[i].set_data(trail_lists[i][0], trail_lists[i][1])


        fig.canvas.draw_idle()
        plt.pause(dt)

    plt.ioff()
    plt.show()


@dataclass
class RegularPolygon:
    n_sides: int
    radius: float = 1.0

    @property
    def vertices(self):
        angles = np.linspace(0, 2 * np.pi, self.n_sides, endpoint=False)
        x = self.radius * np.cos(angles)
        y = self.radius * np.sin(angles)
        return np.column_stack((x, y))
