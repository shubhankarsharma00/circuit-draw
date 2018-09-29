flag_arr=[1,0,0]
import sys
import math
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from display_settings import *
and_gates=[]
v_wire=[]
h_wire=[]




def draw_Wire_vertical():
    for t in v_wire:
        # glClear(GL_COLOR_BUFFER_BIT)
        x=t[0]
        y=t[1]
        glBegin(GL_LINES)
        glColor3fv((1,1,1))
        glVertex2fv((x+40,display_width-(y-20)))
        glVertex2fv((x+40,display_width-(y+20)))    
        glEnd()
    # glFlush()


def draw_Wire_horizontal():
    for t in h_wire:
        # glClear(GL_COLOR_BUFFER_BIT)
        x=t[0]
        y=t[1]
        glBegin(GL_LINES)
        glColor3fv((1,1,1))
        glVertex2fv((x,display_width-(y+20)))
        glVertex2fv((x+40,display_width-(y+20)))    
        glEnd()
    # glFlush()




def drawAnd():
    for t in and_gates:
        # glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POLYGON)
        for i in range(100):
            glColor3fv((1,1,1))
            angle = 2 * 3.14 * i/100  
            x = 15*math.cos(angle)
            y = 20*math.sin(angle)
            glVertex2d(x+t[0]+25,display_width-(y+t[1]+20))
        glEnd()
        # glFlush()
        glBegin(GL_QUADS)
        x=t[0]
        y=t[1]
        for i in range(100):
            glColor3fv((1,1,1))
            glVertex2f(x,display_width-(y))
            glVertex2f(x+25.0,display_width-(y))
            glVertex2f(x+25.0, display_width-(y+40.0))
            glVertex2f(x, display_width-(y+40.0))
        glEnd()
        # glFlush()





def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)





def grid():
    j=0
    while j<display_width+40:
        i=0
        while(i<display_height+40):
            vertices= (
                    (-i, j),
                    (i, j),
                    (i, -j),
                    (-i, -j),
                )   
            # print verticies
            glBegin(GL_LINES)
            glColor3fv(line_color)
            for edge in edges:
                for vertex in edge:
                    glVertex2fv(vertices[vertex])
            glEnd()
            # while j<100:
            #     j+=2
            i+=40
        j+=40




def backGround():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glColor3fv(bg_color)
    glVertex2f( 0.0,0.0)
    glVertex2f( display_height,0.0)
    glVertex2f( display_height, display_width)
    glVertex2f( 0.0, display_width)
    glEnd()




def display():
    global flag_arr
    # print flag_arr[0]
    backGround()
    grid()
    # glClear(GL_COLOR_BUFFER_BIT)
    drawAnd()
    draw_Wire_vertical()
    draw_Wire_horizontal()
        # glFlush()# print i,j
    glFlush()




    
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, w, 0.0, h)

def keyboard(key, x, y):
    global flag_arr
    if key == chr(27):
        sys.exit(0)
    if key == chr(48):
        for i in range(3):
            flag_arr[i]=0
        flag_arr[0]=1
        glutPostRedisplay()
    if key == chr(49):
        for i in range(3):
            flag_arr[i]=0
        flag_arr[1]=1
        glutPostRedisplay()
    if key == chr(50):
        for i in range(3):
            flag_arr[i]=0
        flag_arr[2]=1
        glutPostRedisplay()    
def none():
    pass
def spinDisplay():
    glutPostRedisplay()


def mouse(button, state, x, y):
    global and_gates
    global v_wire
    global h_wire
    x=float(int(x/40))*40
    y=float(int(y/40))*40
    if button == GLUT_LEFT_BUTTON:
        print flag_arr
        if(state == GLUT_DOWN):
            if flag_arr[0]==1:
                and_gates.append((x,y))
            elif flag_arr[1]==1:
                v_wire.append((x,y))
            elif flag_arr[2]==1:
                h_wire.append((x,y))
            glutIdleFunc(spinDisplay)
    elif button == GLUT_MIDDLE_BUTTON or button == GLUT_RIGHT_BUTTON:
        if(state == GLUT_DOWN):
            if and_gates.count((x,y))>0:
                and_gates.remove((x,y))
            if v_wire.count((x,y))>0:    
                v_wire.remove((x,y))
            if h_wire.count((x,y))>0:    
                h_wire.remove((x,y))
            # print "*"         
            glutIdleFunc(spinDisplay)




edges = (
    (0,1),
    (1,2),
    (2,3),
    (0,3)
    )