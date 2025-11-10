import numpy as np


class Pursuer:
    def __init__(self, position: list, velocity: list):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def move(self, dt: float):
        self.position += self.velocity * dt

    def b_a_separation(self, b_position: list) -> list:
        R = b_position - self.position
        return R


class Evader:
    def __init__(self, position: list, velocity: list):
        self.position = np.array(position)
        self.velocity = np.array(velocity)

    def move(self, dt: float):
        self.position += self.velocity * dt
