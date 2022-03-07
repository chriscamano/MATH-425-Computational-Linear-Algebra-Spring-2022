#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 22:15:26 2021

@author: hboateng
Lab due to Dr. J. Humpherys
https://github.com/Foundations-of-Applied-Mathematics/Labs
"""
import numpy as np
from matplotlib import pyplot as plt

# Load the array from the .npy file
#data = np.load("horse.npy")
#print(data)
# Plot the x row against the y row with black pixels
#plt.plot(data[0], data[1], 'k,')

# Set the window limits to [-1,1] by [-1,1] and make the window square
#plt.axis([-1,1,-1,1])
#plt.gca().set_aspect("equal")
#plt.show

class Transformations:
    def __init__(self,data):
        self.x = data[0]
        self.y = data[1]
        
    def display(self):
        plt.plot(self.x, self.y, 'k-,')
        #plt.axis([-1,1,-1,1])
        #plt.gca().set_aspect("equal")
        plt.show
        
    def stretch(self,a,b):
        self.x = a*self.x
        self.y = b*self.y
        
    def shear(self,a,b):
        tempx = self.x
        self.x += a*self.y
        self.y += b*tempx 
        
    def reflect(self,a,b):
        tempx  = self.x
        a2     = a*a
        b2     = b*b  
        ra2pb2 = 1.0/(a2+b2)        
        ra2b2  = (a2-b2)*ra2pb2
        rtab   = -2.0*a*b*ra2pb2
        self.x = -ra2b2*self.x + rtab*self.y
        self.y = rtab*tempx + ra2b2*self.y
        
    def rotate(self,theta):
        cth    = np.cos(theta)
        sth    = np.sin(theta)
        tempx  = self.x
        self.x = cth*self.x - sth*self.y
        self.y = sth*tempx  + cth*self.y
        
    def translate(self,a,b):
        self.x += a
        self.y += b
        
    def compose_stretch_rotate(self,a,b,theta):
        cth    = np.cos(theta)
        sth    = np.sin(theta)
        tempx  = self.x
        self.x = a*cth*self.x - b*sth*self.y
        self.y = a*sth*tempx  + b*cth*self.y

#horse = Transformations(data)   
#horse.stretch(0.5, 1.2) 

#horse.shear(0.5,0)  
#horse.reflect(0,1)
#horse.rotate(np.pi/2)
#horse.translate(0.75, 0.5)
#horse.display()



#horse = Transformations(data)   
#horse.stretch(10.2, 10.2)   
#horse.rotate(np.pi/2)
#plt.subplot(121),horse.display()
"""
horse = Transformations(data)   
horse.compose_stretch_rotate(1.2,1.2,np.pi/2)
plt.subplot(122),horse.display()

"""    