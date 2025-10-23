#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
data = pd.read_csv(csv_file)

angle = 0.0

def main():
    global angle

    if not glfw.init():
        print("Failed to initialize GLFW")
        sys.exit(1)

    window = glfw.create_window(800, 600, "Rotating 3D Spheres", None, None)
    if not window:
        glfw.terminate()
        print("Failed to create GLFW window")
        sys.exit(1)

    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glClearColor(0.1, 0.1, 0.1, 1.0)

    # Enable lighting
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [50.0, 50.0, 100.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    # Perspective projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 1, 1000)
    glMatrixMode(GL_MODELVIEW)

    # Compute center for rotation
    x_min, x_max = data['x'].min(), data['x'].max()
    y_min, y_max = data['y'].min(), data['y'].max()
    z_min, z_max = data['z'].min(), data['z'].max()
    x_center = (x_min + x_max)/2
    y_center = (y_min + y_max)/2
    z_center = (z_min + z_max)/2

    sphere = gluNewQuadric()  # Sphere object

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

        # Draw spheres
        for _, row in data.iterrows():
            glPushMatrix()
            glTranslatef(row['x'], row['y'], row['z'])
            # Material color
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [0.0, 0.6, 1.0, 1.0])
            glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
            glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
            gluSphere(sphere, 1.0, 16, 16)  # radius, slices, stacks
            glPopMatrix()

        glfw.swap_buffers(window)
        glfw.poll_events()

    gluDeleteQuadric(sphere)
    glfw.terminate()

if __name__ == "__main__":
    main()
