#importação das bibliotecas

import numpy #permite trabalhar com matrizes e arrays mult.
from OpenGL.GL import * #modulo PyOpenGL para OpenGL
from OpenGL.GLU import * #modulo PyOpenGL para OpenGL Utility LIbrary
from OpenGL.GLUT import * #modulo PyOpenGL para GLUT(OpenGL Utility Toolkit)
from PIL import Image #manipulação de imagens

#variaveis globais para armazenar as texturas de planetas e satélites
global texture_index, earth, jupiter, mars, mercury, moon, neptune, saturn_ring, saturn, sun, uranus, venus

#carrega as imagens das texturas
def load_images():
    global earth, jupiter, mars, mercury, moon, neptune, saturn_ring, saturn, sun, uranus, venus
    earth = read_texture('./textures/earth.jpg')
    jupiter = read_texture('./textures/jupiter.jpg')
    mars = read_texture('./textures/mars.jpg')
    mercury = read_texture('./textures/mercury.jpg')
    moon = read_texture('./textures/moon.jpg')
    neptune = read_texture('./textures/neptune.jpg')
    saturn_ring = read_texture('./textures/saturn_ring.jpg')
    saturn = read_texture('./textures/saturn.jpg')
    sun = read_texture('./textures/sun.jpg')
    uranus = read_texture('./textures/uranus.jpg')
    venus = read_texture('./textures/venus.jpg')
    return earth, jupiter, mars, mercury, moon, neptune, saturn_ring, saturn, sun, uranus, venus

# função para ler a textura a partir de um arquivo
def read_texture(filename):
    img = Image.open(filename) #armazena imagem carregada a partir do arquivo
    img_data = numpy.array(list(img.getdata()), numpy.int8) 
    textID = glGenTextures(1)

    #configuração dos parâmetros de textura
    glBindTexture(GL_TEXTURE_2D, textID)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    #carrega os dados da imagem como textura
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return textID


