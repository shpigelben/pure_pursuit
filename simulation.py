import numpy as np
from agents import Pursuer, Evader

class Simulation:
    def __init__(self, agents: list, dt: float):
        self.agents = agents
        self.dt = dt

    def run(self):
        for i, agent in enumerate(self.agents):
            if isinstance(agent, Pursuer):
                agent_index = (i+1) % len(self.agents)                                 # if Pursuer update to pursue
                agent.update_velocity(self.agents[agent_index], 'pure_pursuit')        # pursues next agent in list with 'pursuit_method'
            elif isinstance(agent, Evader):                                            # if Evader update to evade                                                
                agent.update_velocity()                                                # evades according to predefined course    
            agent.move(self.dt)                                                        # move agent based on updated velocity and time step
    
    def initial_com(self):
        positions = np.array([agent.position for agent in self.agents])
        mu = positions.mean(axis=0)
        std = positions.std(axis=0)
        return mu, std