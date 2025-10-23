#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Generate sample data if no file is provided
if len(sys.argv) < 2:
    print("No CSV provided, generating random sample data...")
    np.random.seed(0)
    N = 500
    data = np.random.uniform(-10, 10, (N, 3))
else:
    import pandas as pd
    csv_file = sys.argv[1]
    data = pd.read_csv(csv_file).to_numpy()

angle = 0.0

def draw_bounding_cube(min_val=-10, max_val=10):
    glColor3f(1.0, 1.0, 1.0)
    # Bottom face
    glBegin(GL_LINE_LOOP)
    glVertex3f(min_val, min_val, min_val)
    glVertex3f(max_val, min_val, min_val)
    glVertex3f(max_val, max_val, min_val)
    glVertex3f(min_val, max_val, min_val)
    glEnd()
    # Top face
    glBegin(GL_LINE_LOOP)
    glVertex3f(min_val, min_val, max_val)
    glVertex3f(max_val, min_val, max_val)
    glVertex3f(max_val, max_val, max_val)
    glVertex3f(min_val, max_val, max_val)
    glEnd()
    # Vertical edges
    glBegin(GL_LINES)
    glVertex3f(min_val, min_val, min_val)
    glVertex3f(min_val, min_val, max_val)

    glVertex3f(max_val, min_val, min_val)
    glVertex3f(max_val, min_val, max_val)

    glVertex3f(max_val, max_val, min_val)
    glVertex3f(max_val, max_val, max_val)

    glVertex3f(min_val, max_val, min_val)
    glVertex3f(min_val, max_val, max_val)
    glEnd()

def main():
    global angle

    if not glfw.init():
        print("Failed to initialize GLFW")
        sys.exit(1)

    window = glfw.create_window(800, 600, "3D Particles with Bounding Cube", None, None)
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

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 0, 50, 0, 0, 0, 0, 1, 0)

        # Rotate around Y-axis
        glRotatef(angle, 0, 1, 0)
        angle += 0.5
        if angle >= 360.0:
            angle -= 360.0

        # Draw bounding cube
        draw_bounding_cube(-10, 10)

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
