# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:44:03 2020

@author: Nallely
"""


import turtle
import random
import math


VERTICES=[(-1, -0.75, 0), (1.25, -0.5, 0), (0, 1.5, 0)]
TRIANGLES=[(VERTICES[0],VERTICES[1],VERTICES[2])]
def midpoint(a,b,c, roughness, levels):
    mab=[((b[0]+a[0])/2),(((b[1]+a[1])/2)),((b[2]-a[2])/2)]
    mbc=[((c[0]+b[0])/2),(((c[1]+b[1])/2)),((c[2]+b[2])/2)]
    mca=[((a[0]+c[0])/2),(((a[1]+c[1])/2)),((a[2]+c[2])/2)]
    mab[2]+=random.random()*(levels**(-roughness))
    mbc[2]+=random.random()*(levels**(-roughness))
    mca[2]+=random.random()*(levels**(-roughness))
    mab=tuple(mab)
    mbc=tuple(mbc)
    mca=tuple(mca)
    new_vertices=[mab,mbc,mca]
    
    return new_vertices
def midpoint_recursion_function(Vertices,Triangles,levels, roughness):
    
    new_vertices=Vertices
    new_triangles=Triangles
    
    if levels>0:
        new_triangles=[]
        for i in range(len(Triangles)):

            list_midpoints=midpoint(Triangles[i-1][0],Triangles[i-1][1],Triangles[i-1][2], roughness, levels)
            
            resultant_points=[list_midpoints[0],list_midpoints[1],list_midpoints[2]]
            
            new_vertices=list(set(new_vertices+resultant_points))
            
            new_tri1=(Triangles[i-1][0],list_midpoints[0],list_midpoints[2])
            new_tri2=(list_midpoints[0],Triangles[i-1][1],list_midpoints[1])
            new_tri3=(list_midpoints[2],list_midpoints[1],Triangles[i-1][2])
            new_tri4=(list_midpoints[0],list_midpoints[1],list_midpoints[2])
            
            new_triangles+=[new_tri1,new_tri2,new_tri3,new_tri4]
            
    while True:
        
        if levels<1:
            #for i in range(len(new_triangles)):
            #    if new_triangles
            global VERTICES
            global TRIANGLES
            VERTICES=new_vertices
            TRIANGLES=new_triangles
            break
        
        else:
            return midpoint_recursion_function(new_vertices,new_triangles,levels-1, roughness)

midpoint_recursion_function(VERTICES,TRIANGLES,3,1)

for i in range(len(TRIANGLES)):
    TRIANGLES[i]=list(TRIANGLES[i])
    for j in range(len(TRIANGLES[i])):
        TRIANGLES[i][j]=list(TRIANGLES[i][j])
        for k in range(len(VERTICES)):
            VERTICES[k]=list(VERTICES[k])
            if TRIANGLES[i][j]==VERTICES[k]:
                TRIANGLES[i][j]=VERTICES.index(VERTICES[k])
    TRIANGLES[i]=tuple(TRIANGLES[i])

#turtle.screensize(2000,1500)
def transform(x, y, z, angle, tilt):
    #Animation control (around y-axis). If considered as a view of earth from space, it's moving over the equator.
    s, c = math.sin(angle), math.cos(angle)
    x, z = x * c - z * s, x * s + z * c

    #Camera tilt  (around x-axis). If considered as a view of earth from space, the tilt angle is measured from the equator.
    s, c = math.sin(tilt), math.cos(tilt)
    y, z = y * c - z * s, y * s + z * c

    # Setting up View Parameters
    z += 5     #Fixed Distance from top
    FOV = 1000      #Fixed Field of view
    f = FOV / z
    sx, sy = x * f, y * f
    return sx, sy

def main():
    # Create terrain using turtle
    terrain = turtle.Turtle()
    terrain.pencolor("blue")
    terrain.pensize(2)

    # Turn off move time for instant drawing
    turtle.tracer(0, 0)
    terrain.up()
    angle = 0
    
    while True:
        # Clear the screen
        terrain.clear()
        
        # Transform the terrain
        VERT2D = []
        for vert3D in VERTICES:
            x, y, z = vert3D
            sx, sy = transform(x, y, z, angle, 0.25)
            VERT2D.append((sx, sy))

        # Draw the terrain
        for triangle in TRIANGLES:
            points = []
            points.append(VERT2D[triangle[0]])
            points.append(VERT2D[triangle[1]])
            points.append(VERT2D[triangle[2]])

            # Draw the trangle
            terrain.goto(points[0][0], points[0][1])
            terrain.down()

            terrain.goto(points[1][0], points[1][1])
            terrain.goto(points[2][0], points[2][1])
            terrain.goto(points[0][0], points[0][1])
            terrain.up()

        # Update screen
        turtle.update()

        # Control the speed of animation
        angle += 0.005

if __name__ == "__main__":
    main()
