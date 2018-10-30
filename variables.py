from display_settings import *

#for electronical components
and_gates=[]
not_gates=[]
v_wire_down=[]
v_wire_up=[]
h_wire=[]

#flags
flag_bfs=[0,0]
flag_arr=[1,0,0,0,0]

#representing the grid boxes on or off
on,off=[],[]

#for grid
edges = (
    (0,1),
    (1,2),
    (2,3),
    (0,3)
    )
#for graph
g={}
for x in xrange(display_height):
    for y in xrange(display_width):
        g[(x,y)]=[]

visited={}
for x in xrange(display_height):
    for y in xrange(display_width):
        visited[(x,y)]=False
