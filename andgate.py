import sys
import math
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from display_settings import *
import abstraction 
on = abstraction.on
off = abstraction.off

def drawAnd():
#Semicircle of and gate
    for t in abstraction.and_gates:
        # glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POLYGON)
        for i in range(100):
            glColor3fv((1,1,1))
            angle = 2 * 3.14 * i/100  
            x = 15*math.cos(angle)
            y = 20*math.sin(angle)
            glVertex2d(x+t[0]+25,display_width-(y+t[1]+20))
        glEnd()
#Box of gate
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

        x=t[0]-40
        y=t[1]-40
#Upward Vertical in and gate 
        glBegin(GL_LINES)
        col=abstraction.switcher(x-40,y)
        glColor3fv(col)
        glVertex2fv((x+20,display_width-((y+40)-20)))
        glVertex2fv((x+20,display_width-((y+35)+20)))    
        # glVertex2fv((x,display_width-(y+35)))
        # glVertex2fv((x+40,display_width-(y+20)))    
        glVertex2fv((x,display_width-(y+20)))
        glVertex2fv((x+20,display_width-(y+20)))    
        glVertex2fv((x+20,display_width-((y+40)+15)))
        glVertex2fv((x+40,display_width-((y+40)+15)))            

#Downward vertical in and gate
        col=abstraction.switcher(x-40,y+80)
        glColor3fv(col)
        glVertex2fv((x+20,display_width-((y+85)-20)))
        glVertex2fv((x+20,display_width-((y+80)+20)))    
        glVertex2fv((x+20,display_width-(((y+40))+25)))
        glVertex2fv((x+40,display_width-(((y+40))+25)))    
        glVertex2fv((x,display_width-((y+80)+20)))
        glVertex2fv((x+20,display_width-((y+80)+20)))            

#The Output
        if(on.count((x-40,y))>0 and on.count((x-40,y+80))>0):
            glColor3fv((0,1,0))
            abstraction.swi_open((x+120,y+40))
            abstraction.swi_open((x+80,y+40))
        elif(off.count((x-40,y))>0 or off.count((x-40,y+80))>0):
            glColor3fv((1,0,0))
            if on.count((x+80,y+40)):
                on.remove((x+80,y+40))
            abstraction.swi_off((x+120,y+40))
            abstraction.swi_off((x+80,y+40))
        else:                
            glColor3fv((1,1,1))

        glVertex2fv((x+80,display_width-(y+60)))
        glVertex2fv((x+120,display_width-(y+60)))            
        glEnd()

        # glFlush()