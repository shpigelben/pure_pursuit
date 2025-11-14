from agents import Pursuer
from animate import Animate, RegularPolygon
import numpy as np


if __name__ == "__main__":
    # N = 50
    agents = []
    # for i in range(N):
    #     init_pos = np.random.rand(2) * 15
    #     init_vel = np.random.rand(2) * 2
    #     agents.append(Pursuer(position=init_pos, velocity=init_vel))

    polygon = RegularPolygon(n_sides=4, radius=5.0)
    for v in polygon.vertices:
        agents.append(Pursuer(position=v, velocity = np.array([1.0, 0.0])))
    
    
    Animate(agents=agents, dt=0.01, steps=2000)