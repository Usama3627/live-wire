#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:54:47 2019

@author: usama
"""

import cv2 as cv
import numpy as np
import math
from dijkstar import Graph, find_path
import time as t
# Press and hold the mouse to select points
# Press down left click for first point
# Release mouse click for second point
#code starts from here
def click(event, x, y, flags, param):
    global retPt
    # if the left mouse button was clicked, record the starting
	# (x, y) coordinates
    if event == cv.EVENT_LBUTTONDOWN:
        retPt = [(x, y)]
    elif event == cv.EVENT_LBUTTONUP:
        retPt.append((x, y))
	# record the ending (x, y) coordinates
    
    
start_time = t.time()
img = cv.imread("2.jpg", 1)
final = img.copy()
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
vertex = img.copy()
h,w = img.shape[1::-1]

graph = Graph(undirected=True)

# Iterating over an image and avoiding boundaries
for i in range (1, w-1):
    for j in range(1, h-1):
        G_x = float(vertex[i,j]) - float(vertex[i,j+1])    # Center - right
        G_y = float(vertex[i,j]) - float(vertex[i+1, j])   # Center - bottom
        G = np.sqrt((G_x)**2 + (G_y)**2)
        if (G_x > 0 or G_x < 0):
            theeta = math.atan(G_y/G_x)
        # Theeta is rotated in clockwise direction (90 degrees) to align with edge
        theeta_a = theeta + math.pi/2
        G_x_a = abs(G * math.cos(theeta_a)) + 0.00001
        G_y_a = abs(G * math.sin(theeta_a)) + 0.00001
        
        # Strongest Edge will have lowest weights
        W_x = 1/G_x_a
        W_y = 1/G_y_a
        
        # Assigning weights
        graph.add_edge((i,j), (i,j+1), W_x) # W_x is given to right of current vertex
        graph.add_edge((i,j), (i+1,j), W_y) # W_y is given to bottom of current vertex
        
        
print (graph.node_count)
print (graph.edge_count)
print ("Time Taken to turn image to graph: {}".format(t.time()-start_time))
# Opens image select the points using mouse and press c to done
cv.namedWindow("image")
while True:
    while True:
        cv.setMouseCallback("image", click)
        cv.imshow("image", final)
        key = cv.waitKey(2) & 0xFF
        if key == ord("c"):
            #cv.destroyWindow("image")
            break
    # Gets the starts and ending point in image formatss
    print(retPt[0][1], retPt[0][0])
    print(retPt[1][1], retPt[1][0])       
    startPt = (retPt[0][1], retPt[0][0])
    endPt = (retPt[1][1], retPt[1][0])
    
    # Find_path[0] return nodes it travelled for shortest path
    path = find_path(graph,startPt,endPt)[0]
    if path is None:
        break
    # Turn those visited nodes to white
    for i in range(0,len(path)):
        final[path[i][0], path[i][1]] = 255
        
    cv.imshow('ImageWindow', final)
    cv.waitKey(0)
    cv.destroyWindow('ImageWindow')
