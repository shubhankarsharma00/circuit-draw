import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from display_settings import *
import abstraction 
on = abstraction.on
off = abstraction.off

def drawNot():
#Semicircle of and gate
    for t in abstraction.not_gates:
        # glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POLYGON)
        for i in range(100):
            glColor3fv((1,1,1))
            angle = 2 * 3.14 * i/100  
            x = 3*math.cos(angle)
            y = 3*math.sin(angle)
            glVertex2d(x+t[0]+40,display_width-(y+t[1]+20))
        glEnd()
#Box of gate
        x=t[0]
        y=t[1]
        glBegin(GL_QUADS)
        for i in range(50):
            glColor3fv((1,1,1))
            glVertex2f(x,(0.4*i)+(display_width-(y+40.0)))
            glVertex2f(x+i*0.8,(0.4*i)+(display_width-(y+40.0)))
            glVertex2f(x,(display_width-y-(0.4*i)))
            glVertex2f(x+i*0.8,(display_width-y-(0.4*i)))
        glEnd()
        # glFlush()

        x=t[0]
        y=t[1]

#input
        glBegin(GL_LINES)
        if(on.count((x-40,y))>0):
            glColor3fv((0,1,0))
            abstraction.swi_open((x-40,y))
        elif(off.count((x-40,y))>0):
            glColor3fv((1,0,0))
            abstraction.swi_off((x-40,y))
        else:                
            glColor3fv((1,1,1))
        glVertex2fv((x,display_width-(y+20)))
        glVertex2fv((x-40,display_width-(y+20)))            

        x=t[0]
        y=t[1]

#The Output
        if(off.count((x-40,y))>0):
            glColor3fv((0,1,0))
            abstraction.swi_open((x+40,y))
            abstraction.swi_open((x+80,y))
        elif(on.count((x-40,y))>0):
            glColor3fv((1,0,0))
            abstraction.swi_off((x+40,y))
            abstraction.swi_off((x+80,y))
        else:                
            glColor3fv((1,1,1))

        glVertex2fv((x+40,display_width-(y+20)))
        glVertex2fv((x+80,display_width-(y+20)))            
        glEnd()

        # glFlush()