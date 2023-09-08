import sys
import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from texture import load_images

global sunIsActive
global earth, jupiter, mars, mercury, milky_way, moon, neptune, saturn_ring, saturn, sun, uranus, venus
sunIsActive = 1
axisX, axisY, axisZ = 0, 0, 0


def draw_planet(texture, y_pos, x_pos, scale, diameter, radius):
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


def draw_planets_with_satellites(planet_texture, satellite_texture, y_pos, x_pos, scale, planet_diameter, satellite_diameter, planet_radius, moon_radius):
    time = glutGet(GLUT_ELAPSED_TIME) / 1000.0
    rotation_angle = time * 2

    glPushMatrix()
    glRasterPos2f(0, -y_pos)
    glTranslated(0, -y_pos, 0)
    glTranslatef((x_pos * math.cos(2.0 * 3.14 * rotation_angle * planet_radius / 100)),
                 (y_pos + y_pos * math.sin(2.0 * 3.14 * rotation_angle * planet_radius / 100)), 0)
    obj = gluNewQuadric()
    gluQuadricTexture(obj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, planet_texture)
    glScalef(scale, scale, scale)
    glRotated(rotation_angle * 20, 0, 0, 1)
    gluSphere(obj, planet_diameter, 25, 25)

    glTranslatef(x_pos / 10 * (math.cos(2.0 * 3.14 * rotation_angle * moon_radius / 100)),
                 (y_pos / 10 * math.sin(2.0 * 3.14 * rotation_angle * moon_radius / 100)), 0)

    glBindTexture(GL_TEXTURE_2D, satellite_texture)
    glScalef(scale, scale, scale)
    glRotated(rotation_angle * 5, 1, 0, 1)
    gluSphere(obj, satellite_diameter, 50, 50)
    glDisable(GL_TEXTURE_2D)

    glPopMatrix()

def solar_system_with_orbits():
    glDrawBuffer(GL_BACK)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    solar_system() 

def draw_ring(eixoX, eixoY):
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        rad = i * 3.14 / 180
        glVertex2f(math.cos(rad) * eixoX, math.sin(rad) * eixoY)
    glEnd()
    glPopMatrix()

def draw_planets_with_satellites_and_rings(planet_texture, satellite_texture, rings_texture, y_pos, x_pos, scale, planet_diameter, satellite_diameter, radius, moon_radius):

    time = glutGet(GLUT_ELAPSED_TIME) / 1000.0
    rotation_angle = time * 2

    glPushMatrix()
    glRasterPos2f(0, -y_pos)
    glTranslated(0, -y_pos, 0)
    glTranslatef((x_pos * math.cos(2.0 * 3.14 * rotation_angle * radius / 100)),
                 (y_pos + y_pos * math.sin(2.0 * 3.14 * rotation_angle * radius / 100)), 0)
    obj = gluNewQuadric()
    gluQuadricTexture(obj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, planet_texture)
    glScalef(scale, scale, scale)
    glRotated(rotation_angle * 20, 0, 0, 1)
    gluSphere(obj, planet_diameter, 25, 25)
    glScalef(scale, scale, scale)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, rings_texture)
    draw_ring(x_pos/80, y_pos/80)

    glTranslatef(x_pos/20*(math.cos(2.0 * 3.14 * rotation_angle * moon_radius / 100)),
                 (y_pos/20*math.sin(2.0 * 3.14 * rotation_angle * moon_radius / 100)), 0)
    glBindTexture(GL_TEXTURE_2D, satellite_texture)
    glScalef(scale, scale, scale)
    glRotated(rotation_angle * 5, 1, 0, 1)
    gluSphere(obj, satellite_diameter, 50, 50)
    glDisable(GL_TEXTURE_2D)

    glPopMatrix()  


def solar_system():
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
    draw_planet(mercury, 7, 7, 2, 0.48, 3.7)

    # VENUS - Diameter: 12,103.6 km
    draw_planet(venus, 17, 17, 1.2, 1.21, 2.5)

    # EARTH AND MOON - Diameter Earth: 12,756.2 km
    draw_planets_with_satellites(
        earth, moon, 27, 27, 1.2, 1.27, 0.5, 1.9, 0.2)

    # MARS - Diameter: 6,792.4 km
    draw_planets_with_satellites(mars, moon, 41, 41, 1.2, 0.68, 0.5, 1.9, 1)

    # URANUS - Diameter: 51,118 km
    draw_planets_with_satellites(
        uranus, moon, 107, 107, 1.5, 0.51, 0.25, 1.2, 1.3)

    # NEPTUNE - Diameter: 49,528 km
    draw_planets_with_satellites(
        neptune, moon, 127, 127, 1.5, 0.495, 0.20, 1, 1)
    
    # JUPITER - Diameter: 142,984 km
    draw_planets_with_satellites_and_rings(
        jupiter, moon, saturn_ring, 80, 80, 1.5, 1.43, 0.25, 1.9, 1)

    # SATURN - Diameter: 120,536 km
    draw_planets_with_satellites_and_rings(
        saturn, moon, saturn_ring, 97, 97, 1.5, 1.2, 0.25, 1.5, 1)

    glRasterPos2f(0, -51)


def draw():
    glDrawBuffer(GL_BACK)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    solar_system()
    glutSwapBuffers()


def initialize():
    global angle, rotX, rotY, rotZ, obsX, obsY, obsZ
    global earth, jupiter, mars, mercury, moon, neptune, saturn_ring, saturn, sun, uranus, venus

    angle = 10

    rotX = 0
    rotY = 0
    rotZ = 0
    obsX = obsY = 0
    obsZ = 150

    earth, jupiter, mars, mercury, moon, neptune, saturn_ring, saturn, sun, uranus, venus = load_images()

    glEnable(GL_CULL_FACE)  
    glCullFace(GL_BACK)  

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)


def main():
    glutInit(sys.argv)
    glutInitContextVersion(1, 1)
    glutInitContextProfile(GLUT_COMPATIBILITY_PROFILE)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Sistema Solar")

    glutDisplayFunc(solar_system_with_orbits)

    initialize()


main()
