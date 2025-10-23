#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np

def generate_mountain_data(n_points=100, x_range=(-10, 10), z_range=(-10, 10), peak_height=10.0, randomness=1.0):
    """
    Generate simple mountain-like 3D data.
    x, z are horizontal; y is vertical (height).
    """
    # Random horizontal positions
    xs = np.random.uniform(x_range[0], x_range[1], n_points)
    zs = np.random.uniform(z_range[0], z_range[1], n_points)
    
    # Compute height (y) as a Gaussian hill
    dist = np.sqrt(xs**2 + zs**2)
    ys = peak_height * np.exp(-0.05 * dist**2) + np.random.uniform(-randomness, randomness, n_points)
    
    # Stack columns in x, y, z order
    data = np.column_stack((xs, ys, zs))
    return data

def main():
    # Number of points from first CLI arg, default 100
    n_points = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    data = generate_mountain_data(n_points=n_points)
    
    # Output CSV to stdout
    print("x,y,z")
    for row in data:
        print(f"{row[0]:.3f},{row[1]:.3f},{row[2]:.3f}")

if __name__ == "__main__":
    main()
