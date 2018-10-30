import sys
import math
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from display_settings import *
import abstraction 
on = abstraction.on
off = abstraction.off
v_wire_up = abstraction.v_wire_up
v_wire_down = abstraction.v_wire_down



#Draws vertical wires

def draw_Wire_vertical():
    for t in v_wire_up:
        x=t[0]
        y=t[1]-40
        glBegin(GL_LINES)
        col = switcher(t)
        glColor3fv(col)
        glVertex2fv((x+20,display_width-(((y+40))+20)))
        glVertex2fv((x+40,display_width-(((y+40))+20)))    
        glVertex2fv((x,display_width-((y+80)+20)))
        glVertex2fv((x+20,display_width-((y+80)+20)))            
        glVertex2fv((x+20,display_width-((y+80)-20)))
        glVertex2fv((x+20,display_width-((y+80)+20)))    
        glEnd()
    for t in v_wire_down:
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

