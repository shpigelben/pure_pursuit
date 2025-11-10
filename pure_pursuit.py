import numpy as np


def pure_pursuit(a, b):
    R = b.position - a.position
    new_dir = np.arctan2(R[1], R[0])
    a.velocity = np.linalg.norm(a.velocity) * np.array(
        [np.cos(new_dir), np.sin(new_dir)]
    )
