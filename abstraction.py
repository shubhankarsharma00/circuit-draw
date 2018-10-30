from variables import *
import sys
import math
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from display_settings import *
from andgate import *
from verticalwire import *
from notgate import *

def setflag(x):
    for i in range(5):
        flag_arr[i]=0
    flag_arr[x]=1

def setflagbfs(x):
    for i in range(5):
        flag_arr[i]=0
    flag_bfs[x]=1

def switcher(x,y):
    if(on.count((x,y))>0):
        return (0,1,0)
    elif(off.count((x,y))>0):
        return(1,0,0)
    else:
        return(1,1,1)


def swi_open((x,y)):
    if(off.count((x,y))>0):
        off.remove((x,y))
    if(on.count((x,y))==0):
        on.append((x,y))

def swi_off((x,y)):
    if(on.count((x,y))>0):
        on.remove((x,y))
    if(off.count((x,y))==0):
        off.append((x,y))

def clear():
    for x in xrange(display_height):
        for y in xrange(display_width):
            visited[(x,y)]=False


def bfs((x,y)):
    global flag_bfs
    if(flag_bfs[1]==1):
        swi_off((x,y))
        queue=[(x,y)]
        while(len(queue)!=0):
            p=queue[0]
            visited[p]=True
            queue.remove(p)
            for i in g[p]:    
                if(visited[i]==False):
                    queue.append(i)
                    visited[i]=True
                    bfs(i)
    else:
        swi_open((x,y))
        queue=[(x,y)]
        while(len(queue)!=0):
            p=queue[0]
            visited[p]=True
            queue.remove(p)
            for i in g[p]:    
                if(visited[i]==False):
                    queue.append(i)
                    visited[i]=True
                    bfs(i)
            



def draw_Wire_horizontal():
    for t in h_wire:
        # print "hey"
        # glClear(GL_COLOR_BUFFER_BIT)
        x=t[0]
        y=t[1]
        # print t,on.count(t),off.count(t)
        if(on.count(t)>0 or on.count((x+40,y))>0 or on.count((x-40,y))>0):
            glColor3fv((0,1,0))
            swi_open((x,y))
        elif(off.count(t)>0 or off.count((x+40,y))>0 or off.count((x-40,y))>0):
            glColor3fv((1,0,0))
            swi_off((x,y))
        else:    
            glColor3fv((1,1,1))
        glBegin(GL_LINES)
        glVertex2fv((x,display_width-(y+20)))
        glVertex2fv((x+40,display_width-(y+20)))            
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
    # print on,off
    backGround()
    grid()
    # glClear(GL_COLOR_BUFFER_BIT)
    drawAnd()
    drawNot()
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
    global flag_bfs
    if key == chr(27):
        sys.exit(0)
    if key =='a':
        setflag(0)
        glutPostRedisplay()
    elif key =='V':
        setflag(1)
        glutPostRedisplay()
    elif key =='h':
        setflag(2)
        glutPostRedisplay()    
    elif key == 'v':
        setflag(3)
        glutPostRedisplay()    
    elif key == 'n':
        setflag(4)
        glutPostRedisplay()  
    elif key == 'g':
        setflagbfs(0)
        glutPostRedisplay()    
    elif key == 'r':
        setflagbfs(1)
        glutPostRedisplay()    
def none():
    pass
    
def spinDisplay():
    glutPostRedisplay()

def mouse(button, state, x, y):
    global and_gates
    global v_wire_down
    global v_wire_up
    global h_wire
    global flag_bfs
    x=float(int(x/40))*40
    y=float(int(y/40))*40
    if button == GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            # print flag_arr
            if flag_bfs[0]==1:
                clear()
                bfs((x,y))
                flag_bfs[0]=0
                # print sorted(on),sorted(off)
            elif flag_bfs[1]==1:
                clear()
                bfs((x,y))
                flag_bfs[1]=0
                # print sorted(on),sorted(off)
            elif flag_arr[0]==1:
                and_gates.append((x,y))
            elif flag_arr[4]==1:
                not_gates.append((x,y))
            elif flag_arr[1]==1:
                v_wire_down.append((x,y))
                g[(x,y)].append((x-40,y-40))
                g[(x,y)].append((x+40,y))
                g[(x-40,y-40)].append((x,y))
                g[(x+40,y)].append((x,y))
            elif flag_arr[3]==1:
                v_wire_up.append((x,y))
                g[(x,y)].append((x-40,y+40))
                g[(x,y)].append((x+40,y))
                g[(x-40,y+40)].append((x,y))
                g[(x+40,y)].append((x,y))
            elif flag_arr[2]==1:
                h_wire.append((x,y))
                g[(x,y)].append((x+40,y))
                g[(x,y)].append((x-40,y))
                g[(x+40,y)].append((x,y))
                g[(x+40,y)].append((x-40,y))
                g[(x-40,y)].append((x,y))
                g[(x-40,y)].append((x+40,y))
            glutIdleFunc(spinDisplay)
    elif button == GLUT_MIDDLE_BUTTON or button == GLUT_RIGHT_BUTTON:
        if(state == GLUT_DOWN):
            if and_gates.count((x,y))>0:
                and_gates.remove((x,y))
            if not_gates.count((x,y))>0:
                not_gates.remove((x,y))
            if h_wire.count((x,y))>0:    
                h_wire.remove((x,y))
            if on.count((x,y))>0:
                on.remove((x,y))
            if off.count((x,y))>0:
                off.remove((x,y))
            if v_wire_up.count((x,y))>0:    
                v_wire_up.remove((x,y))
            if v_wire_down.count((x,y))>0:    
                v_wire_down.remove((x,y))
            # print "*"         
            glutIdleFunc(spinDisplay)
