#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        print("Failed to initialize GLFW")
        sys.exit(1)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Triangle", None, None)
    if not window:
        glfw.terminate()
        print("Failed to create GLFW window")
        sys.exit(1)

    glfw.make_context_current(window)

    # Define a simple render loop
    while not glfw.window_should_close(window):
        glClearColor(0.3, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()
        glTranslatef(-0.5, -0.5, 0.0)

        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(0.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(0.0, 1.0)
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
