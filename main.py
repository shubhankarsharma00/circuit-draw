from abstraction import *
from display_settings import *
title="Desi StImUlAtOr"
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(display_height, display_width)
glutInitWindowPosition(100, 100)
glutCreateWindow(title)
init()
#Display Fun
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
glutMainLoop()
