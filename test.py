from abstraction import *
from display_settings import *
import math
title="Desi Simulator"
def display2():
	glClear(GL_COLOR_BUFFER_BIT)
	x=160
	y=120
	glBegin(GL_LINES)
	glColor3fv((1,1,1))
	glVertex2fv((x,y+20))
	glVertex2fv((x+40,y+20))	
	glEnd()
	glFlush()
	
#Functions to test the software	
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(display_height, display_width)
glutInitWindowPosition(100, 100)
glutCreateWindow(title)
init()
glutDisplayFunc(display2)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
glutMainLoop()
