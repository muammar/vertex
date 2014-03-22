#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Muammar El Khatib"
__copyright__ = "Copyright 2014, Muammar El Khatib"
__credits__ = [""]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Muammar El Khatib"
__email__ = "muammarelkhatib@gmail.com"
__status__ = "Development"
"""

data=[]
n=3
print('Enter your data')
for i in range(0,n):
    x = input()
    data.append(x)

print ('Your entered points')
print ('')
print (data)

denom=(data[0][0] - data[1][0]) * (data[0][0] - data[2][0]) * (data[1][0] - data[2][0])
a=(data[2][0] * (data[1][1] - data[0][1]) + data[1][0] * (data[0][1] - data[2][1]) + data[0][0] * (data[2][1] - data[1][1])) / denom
b=(data[2][0]*data[2][0] * (data[0][1] - data[1][1]) + data[1][0]*data[1][0] * (data[2][1] - data[0][1]) + data[0][0]*data[0][0] * (data[1][1] - data[2][1])) / denom
c=(data[1][0] * data[2][0] * (data[1][0] - data[2][0]) * data[0][1] + data[2][0] * data[0][0] * (data[2][0] - data[0][0]) * data[1][1] + data[0][0] * data[1][0] * (data[0][0] - data[1][0]) * data[2][1]) / denom


xv=-b/(2*a)
yv=c-b*b/(4*a)
vertex=(xv,yv)

print ('The coordinate of the parabola is:') + str(vertex)
