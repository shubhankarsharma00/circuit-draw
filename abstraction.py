flag_bfs=[0,0]
flag_arr=[1,0,0,0]
on,off=[],[]
import sys
import math
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from display_settings import *
and_gates=[]
v_wire_down=[]
v_wire_up=[]
h_wire=[]
<<<<<<< HEAD
edges = (
    (0,1),
    (1,2),
    (2,3),
    (0,3)
    )
g={}
for x in xrange(display_height):
    for y in xrange(display_width):
        g[(x,y)]=[]

visited={}
for x in xrange(display_height):
    for y in xrange(display_width):
        visited[(x,y)]=False

def swi_open((x,y)):
    if(on.count((x,y))==0):
        on.append((x,y))

def swi_off((x,y)):
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
        if(on.count((x,y))>0):
            on.remove((x,y))
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
        if(off.count((x,y))>0):
            off.remove((x,y))
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
            
=======


#Draws vertical wires
>>>>>>> 6561deec8a34f69199e311d04867888535ce65fe

def draw_Wire_vertical():
    for t in v_wire_up:
        # glClear(GL_COLOR_BUFFER_BIT)
        x=t[0]
        y=t[1]-40
        glBegin(GL_LINES)
        if(on.count(t)>0):
            glColor3fv((0,1,0))
        elif(off.count(t)>0):
            glColor3fv((1,0,0))
        else:    
            glColor3fv((1,1,1))
        glVertex2fv((x+20,display_width-(((y+40))+20)))
        glVertex2fv((x+40,display_width-(((y+40))+20)))    
        glVertex2fv((x,display_width-((y+80)+20)))
        glVertex2fv((x+20,display_width-((y+80)+20)))            
        glVertex2fv((x+20,display_width-((y+80)-20)))
        glVertex2fv((x+20,display_width-((y+80)+20)))    
        glEnd()
    for t in v_wire_down:
        # glClear(GL_COLOR_BUFFER_BIT)
        x=t[0]
        y=t[1]-40
        glBegin(GL_LINES)
        if(on.count(t)>0):
            glColor3fv((0,1,0))
        elif(off.count(t)>0):
            glColor3fv((1,0,0))
        else:    
            glColor3fv((1,1,1))
        glVertex2fv((x+20,display_width-((y+40)-20)))
        glVertex2fv((x+20,display_width-((y+40)+20)))    
        glVertex2fv((x,display_width-(y+20)))
        glVertex2fv((x+20,display_width-(y+20)))    
        glVertex2fv((x+20,display_width-((y+40)+20)))
        glVertex2fv((x+40,display_width-((y+40)+20)))            
        glEnd()
    # glFlush()

<<<<<<< HEAD
=======
#draw horizontal wires
>>>>>>> 6561deec8a34f69199e311d04867888535ce65fe
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
        x=t[0]-40
        y=t[1]-40
        glBegin(GL_LINES)
        if(on.count((x-40,y))>0):
            glColor3fv((0,1,0))
        elif(off.count((x-40,y))>0):
            glColor3fv((1,0,0))
        else:
            glColor3fv((1,1,1))
        glVertex2fv((x+20,display_width-((y+40)-20)))
        glVertex2fv((x+20,display_width-((y+35)+20)))    
        # glVertex2fv((x,display_width-(y+35)))
        # glVertex2fv((x+40,display_width-(y+20)))    
        glVertex2fv((x,display_width-(y+20)))
        glVertex2fv((x+20,display_width-(y+20)))    
        glVertex2fv((x+20,display_width-((y+40)+15)))
        glVertex2fv((x+40,display_width-((y+40)+15)))            

        if(on.count((x-40,y+80))>0):
            glColor3fv((0,1,0))
        elif(off.count((x-40,y+80))>0):
            glColor3fv((1,0,0))
        else:
            glColor3fv((1,1,1))
        glVertex2fv((x+20,display_width-((y+85)-20)))
        glVertex2fv((x+20,display_width-((y+80)+20)))    
        # glVertex2fv((x,display_width-(y+35)))
        # glVertex2fv((x+40,display_width-(y+20)))    
        glVertex2fv((x+20,display_width-(((y+40))+25)))
        glVertex2fv((x+40,display_width-(((y+40))+25)))    
        glVertex2fv((x,display_width-((y+80)+20)))
        glVertex2fv((x+20,display_width-((y+80)+20)))            
        if(on.count((x-40,y))>0 and on.count((x-40,y+80))>0):
            glColor3fv((0,1,0))
            swi_open((x+80,y+40))
        elif(off.count((x-40,y))>0 or off.count((x-40,y+80))>0):
            glColor3fv((1,0,0))
            if on.count((x+80,y+40)):
                on.remove((x+80,y+40))
            swi_off((x+80,y+40))

        else:                
            glColor3fv((1,1,1))

        glVertex2fv((x+80,display_width-(y+60)))
        glVertex2fv((x+120,display_width-(y+60)))            
        glEnd()
        x=t[0]
        y=t[1]
        glBegin(GL_QUADS)
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
    # print on,off
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
    global flag_bfs
    if key == chr(27):
        sys.exit(0)
    if key =='a':
        for i in range(4):
            flag_arr[i]=0
        flag_arr[0]=1
        glutPostRedisplay()
    elif key =='V':
        for i in range(4):
            flag_arr[i]=0
        flag_arr[1]=1
        glutPostRedisplay()
    elif key =='h':
        for i in range(4):
            flag_arr[i]=0
        flag_arr[2]=1
        glutPostRedisplay()    
    elif key == 'v':
        for i in range(4):
            flag_arr[i]=0
        flag_arr[3]=1
        glutPostRedisplay()    
    elif key == 'g':
        for i in range(4):
            flag_arr[i]=0
        flag_bfs[0]=1 
        glutPostRedisplay()    
    elif key == 'r':
        for i in range(4):
            flag_arr[i]=0
        flag_bfs[1]=1 
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
                print sorted(on),sorted(off)
            elif flag_bfs[1]==1:
                clear()
                bfs((x,y))
                flag_bfs[1]=0
                print sorted(on),sorted(off)
            elif flag_arr[0]==1:
                and_gates.append((x,y))
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
<<<<<<< HEAD
=======




edges = (
    (0,1),
    (1,2),
    (2,3),
    (0,3)
    )
>>>>>>> 6561deec8a34f69199e311d04867888535ce65fe
