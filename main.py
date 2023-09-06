import sys
import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global sunIsActive
global earth, jupiter, mars, mercury, milky_way, moon, neptune, saturn_ring, saturn, sun, uranus, venus
sunIsActive = 1
axisX, axisY, axisZ = 0, 0, 0


def Draw_Planet(texture, y_pos, x_pos, scale, diameter, radius):
    time = glutGet(GLUT_ELAPSED_TIME) / 1000.0
    rotation_angle = time * 2

    glPushMatrix()
    glRasterPos2f(0, -y_pos)
    glTranslated(0, -y_pos, 0)
    # Translation
    glTranslatef((x_pos * math.cos(2.0 * 3.14 * rotation_angle * radius / 100)),
                 (y_pos + y_pos * math.sin(2.0 * 3.14 * rotation_angle * radius / 100)), 0)
    obj = gluNewQuadric()
    gluQuadricTexture(obj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    glScalef(scale, scale, scale)
    glRotated(rotation_angle * 20, 0, 0, 1)
    gluSphere(obj, diameter, 25, 25)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()



def Solar_System_with_orbits():
    glDrawBuffer(GL_BACK)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Solar_System()


def Solar_System():
    global mercury, venus

    time = glutGet(GLUT_ELAPSED_TIME) / 1000.0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if (sunIsActive == 1):
        ambiente_light = [axisX, axisY, axisZ, 1.0]
        diffuse_light = [axisX, axisY, axisZ, 1.0]
        specular_light = [axisX, axisY, axisZ, 1.0]
        position_light = [1.0, 0.0, 0.0, 1.0]

        ambient_mat = [0.7, 0.7, 0.7, 1.0]
        diffuse_mat = [0.8, 0.8, 0.8, 1.0]
        specular_mat = [1.0, 1.0, 1.0, 1.0]
        high_shininess = [100.0]

        glShadeModel(GL_SMOOTH)

        glLightfv(GL_LIGHT0, GL_AMBIENT, ambiente_light)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
        glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)
        glLightfv(GL_LIGHT0, GL_POSITION, position_light)

        glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)

        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)

        glPushMatrix()
        glRasterPos2f(0, 1.5)
        qobj = gluNewQuadric()
        gluQuadricTexture(qobj, GL_TRUE)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, sun)
        glMaterialfv(GL_FRONT, GL_AMBIENT, ambient_mat)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse_mat)
        glMaterialfv(GL_FRONT, GL_SPECULAR, specular_mat)
        glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)
        glRotated(time * 7, 0, 0, 1)
        glScalef(3, 3, 3)
        gluSphere(qobj, 1, 25, 25)
        glPopMatrix()  # End of push
        glDisable(GL_TEXTURE_2D)

    else:
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
    
    # MERCURY - Diameter: 4,879.4 km
    Draw_Planet(mercury, 7, 7, 2, 0.48, 3.7)

    # VENUS - Diameter: 12,103.6 km
    Draw_Planet(venus, 17, 17, 1.2, 1.21, 2.5)

    glRasterPos2f(0, -51)


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
