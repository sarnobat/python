#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]

# Load CSV using standard library
data = []
with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    try:
        # Check if header is numeric
        [float(x) for x in header]
        # Header is actually data
        data.append([float(x) for x in header])
    except ValueError:
        # Skip header
        pass
    for row in reader:
        data.append([float(x) for x in row])

angle = 0.0

def main():
    global angle

    if not glfw.init():
        print("Failed to initialize GLFW")
        sys.exit(1)

    window = glfw.create_window(800, 600, "Rotating 3D Particles", None, None)
    if not window:
        glfw.terminate()
        print("Failed to create GLFW window")
        sys.exit(1)

    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    glPointSize(5.0)
    glClearColor(0.1, 0.1, 0.1, 1.0)

    # Perspective projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 1, 1000)
    glMatrixMode(GL_MODELVIEW)

    # Compute scale to center particles
    xs, ys, zs = zip(*data)
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    z_min, z_max = min(zs), max(zs)
    x_center = (x_min + x_max)/2
    y_center = (y_min + y_max)/2
    z_center = (z_min + z_max)/2

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)

        # Rotate around Y-axis
        glTranslatef(-x_center, -y_center, -z_center)
        glRotatef(angle, 0, 1, 0)
        glTranslatef(x_center, y_center, z_center)
        angle += 0.5
        if angle >= 360.0:
            angle -= 360.0

        # Draw particles
        glBegin(GL_POINTS)
        for x, y, z in data:
            glColor3f(0.0, 0.6, 1.0)
            glVertex3f(x, y, z)
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
