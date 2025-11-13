import numpy as np

class Simulation:
    def __init__(self, agents: list, dt: float):
        self.agents = agents
        self.dt = dt

    def run(self):
        for i, agent in enumerate(self.agents):
            agent.update_velocity(self.agents[(i+1) % len(self.agents)], 'pure_pursuit')
            agent.move(self.dt)
    
    def initial_com(self):
        positions = np.array([agent.position for agent in self.agents])
        mu = positions.mean(axis=0)
        std = positions.std(axis=0)
        return mu, std

# if __name__ == "__main__":

#     p1 = Pursuer(position=[0.0, 0.0], velocity=[0.0, 1.0])
#     e1 = Evader(position=[-4.0, 4.0], velocity=[0.5, 0.5])

#     dt = 0.01
#     steps = 2000

#     plt.ion()
#     fig, ax = plt.subplots()
#     ax.set(xlabel="x", ylabel="y")
#     mu = (p1.position + e1.position) / 2
#     sigma = 0.5*(np.sqrt(np.sum((p1.position - e1.position)**2)))
#     L = sigma*4
#     ax.set(xlim=(mu[0]-L, mu[0]+L), ylim=(mu[1]-L,mu[1]+L))

#     pursuer_location = ax.scatter([], [], s=40, color="crimson")
#     evader_location = ax.scatter([], [], s=40, color="royalblue")
    
#     pursuer_trail_line, = ax.plot([], [], linewidth=1, color="crimson")
#     evader_trail_line, = ax.plot([], [], linewidth=1, color="royalblue")
    
#     pursuer_trail_list = [[], []]
#     evader_trail_list = [[], []]
    
#     for step in range(steps):
#         pursuit.pure_pursuit(p1, e1)
#         p1.move(dt)
#         e1.move(dt)
        
#         pursuer_trail_list[0].append(p1.position[0])
#         pursuer_trail_list[1].append(p1.position[1])
#         evader_trail_list[0].append(e1.position[0])
#         evader_trail_list[1].append(e1.position[1])

#         pursuer_location.set_offsets(p1.position)
#         evader_location.set_offsets(e1.position)
#         pursuer_trail_line.set_data(pursuer_trail_list[0], pursuer_trail_list[1])
#         evader_trail_line.set_data(evader_trail_list[0], evader_trail_list[1])


#         fig.canvas.draw_idle()
#         plt.pause(dt)

#     plt.ioff()
#     plt.show()
