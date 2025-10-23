#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

def generate_mountain_data(n_points=100, x_range=(-10, 10), y_range=(-10, 10), peak_height=10.0, randomness=1.0):
    """
    Generate a simple mountain-shaped 3D dataset.
    
    Parameters:
    - n_points: int, total number of points
    - x_range: tuple, min and max for x
    - y_range: tuple, min and max for y
    - peak_height: float, approximate maximum height at center
    - randomness: float, noise amplitude
    
    Returns:
    - Nx3 numpy array with columns [x, y, z]
    """
    # Sample points uniformly in x and y
    xs = np.random.uniform(x_range[0], x_range[1], n_points)
    ys = np.random.uniform(y_range[0], y_range[1], n_points)

    # Distance from center (0,0)
    dist = np.sqrt(xs**2 + ys**2)

    # Compute a "mountain" height profile: peak at center, decays outward
    z = peak_height * np.exp(-0.05 * dist**2)

    # Add some randomness
    z += np.random.uniform(-randomness, randomness, n_points)

    # Stack into Nx3 array
    data = np.column_stack((xs, ys, z))
    return data

if __name__ == "__main__":
    # Read number of points from CLI arg, default 100
    n_points = int(sys.argv[1]) if len(sys.argv) > 1 else 100

    data = generate_mountain_data(n_points=n_points)

    # Print CSV header
    print("x,y,z")
    # Print data rows
    for row in data:
        print(f"{row[0]:.3f},{row[1]:.3f},{row[2]:.3f}")
