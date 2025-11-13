import numpy as np
from dataclasses import dataclass

@dataclass
class Agent:
    position: np.ndarray
    velocity: np.ndarray

    def __post_init__(self):
        self.position = np.array(self.position, dtype=float)
        self.velocity = np.array(self.velocity, dtype=float)

    def move(self, dt: float):
        self.position += self.velocity * dt


class Pursuer(Agent):

    def update_velocity(self,
                        target: 'Agent',
                        pursuit_method: str):
        
        if pursuit_method == 'pure_pursuit':
            direction = target.position - self.position
            norm = np.linalg.norm(direction)
            if norm < 1e-9:
                return

            speed = np.linalg.norm(self.velocity)
            self.velocity = speed * direction / norm


class Evader(Agent):
    pass
