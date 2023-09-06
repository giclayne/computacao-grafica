import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def Solar_System_with_orbits():
    glDrawBuffer(GL_BACK)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Solar_System()
    Show_Orbits()


def main():
    glutInit(sys.argv)
    glutInitContextVersion(1, 1)
    glutInitContextProfile(GLUT_COMPATIBILITY_PROFILE)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Sistema Solar")

    glutDisplayFunc(Solar_System_with_orbits)


main()
