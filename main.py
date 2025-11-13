from pursuer_evador import Pursuer
from animate import Animate
import numpy as np

N = 50
if __name__ == "__main__":
    agents = []
    for i in range(N):
        init_pos = np.random.rand(2) * 15
        init_vel = np.random.rand(2) * 2
        agents.append(Pursuer(position=init_pos, velocity=init_vel))

    Animate(agents=agents, dt=0.01, steps=2000)