import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


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
