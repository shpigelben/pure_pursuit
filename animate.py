import matplotlib.pyplot as plt
from simulation import Simulation

def Animate(agents, dt, steps):
    sim = Simulation(agents, dt)

    plt.ion()
    fig, ax = plt.subplots()
    
    colors = [plt.get_cmap('tab10')(i) for i in range(len(agents))]
    mu, std = sim.initial_com()
    L = 10
    ax.set(xlim = (mu[0]-L, mu[0]+L), 
           ylim = (mu[1]-L, mu[1]+L))
    

    locations = [ax.scatter([], [], s=40, color = colors[i]) 
                for i in range(len(agents))]
    # trail_lines = [ax.plot([], [], linewidth=1)[0] for _ in agents]
    # trail_lists = [[[], []] for _ in agents]
    for _ in range(steps):
        sim.run()
        for i, agent in enumerate(agents):
            locations[i].set_offsets(agent.position)
            # print(agent.position)
            # trail_lists[i][0].append(agent.position[0])
            # trail_lists[i][1].append(agent.position[1])
            # trail_lines[i].set_data(trail_lists[i][0], trail_lists[i][1])


        fig.canvas.draw_idle()
        plt.pause(dt)

    plt.ioff()
    plt.show()

# class Animate:
#     def __init__(self, agents, dt, steps):

#     plt.ion()
#     fig, ax = plt.subplots()
#     mu = (a.position + b.position + c.position) / 3
#     L = 1
#     ax.set(xlim=(mu[0] - L, mu[0] + L), ylim=(mu[1] - L, mu[1] + 2*L))

#     a_location = ax.scatter([], [], s=40, color="crimson")
#     b_location = ax.scatter([], [], s=40, color="royalblue")
#     c_location = ax.scatter([], [], s=40, color="forestgreen")

#     (a_trail_line,) = ax.plot([], [], linewidth=1, color="crimson")
#     (b_trail_line,) = ax.plot([], [], linewidth=1, color="royalblue")
#     (c_trail_line,) = ax.plot([], [], linewidth=1, color="forestgreen")

#     a_trail_list = [[], []]
#     b_trail_list = [[], []]
#     c_trail_list = [[], []]

#     for step in range(steps):
#         a.update_velocity(b, 'pure_pursuit')
#         b.update_velocity(c, 'pure_pursuit')
#         c.update_velocity(a, 'pure_pursuit')

#         a.move(dt)
#         b.move(dt)
#         c.move(dt)

#         a_trail_list[0].append(a.position[0])
#         a_trail_list[1].append(a.position[1])
#         b_trail_list[0].append(b.position[0])
#         b_trail_list[1].append(b.position[1])
#         c_trail_list[0].append(c.position[0])
#         c_trail_list[1].append(c.position[1])

#         a_location.set_offsets(a.position)
#         b_location.set_offsets(b.position)
#         c_location.set_offsets(c.position)
#         a_trail_line.set_data(a_trail_list[0], a_trail_list[1])
#         b_trail_line.set_data(b_trail_list[0], b_trail_list[1])
#         c_trail_line.set_data(c_trail_list[0], c_trail_list[1])

#         fig.canvas.draw_idle()
#         plt.pause(dt)

#     plt.ioff()
#     plt.show()
