#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 19:22:42 2018

@author: nishimehta

"""

import cv2
import numpy

# performs convolution between matrix m and k
def convolution(m,k):
    product=0
    n=len(m)-1
    for i in range(len(m)):
        for j in range(len(m)):
            product+=(m[i][j] * k[(n-i)][n-j])
    return product

# extracts matrix of size nxn from matrix mat around position i,j
def extract_matrix(i,j,mat,n):
    x = int(n/2)
    extract=[[0 for x in range(n)] for y in range(n)] 
    for k in range(n):
        for l in range(n):
            extract[k][l] = mat[i-x+k][j-x+l]
    return extract

#pads image with n rows and columns with value as 0
def image_padding(im,n):
    
    for j in range(int(n/2)):
        for i in range(len(im)):
            im[i].insert(0,0)
    for j in range(int(n/2)):
        for i in range(len(im)):
            im[i].insert(len(im[i]),0)
            
    for i in range(int(n/2)):
        zeroes_list = [0 for x in range(len(im[0]))]
        im.insert(len(im),zeroes_list)
    for i in range(int(n/2)):
        zeroes_list = [0 for x in range(len(im[0]))]
        im.insert(0,zeroes_list)
    return im

#applies the filter to the image
def apply_filter(im,filter):
    image_padding(im,len(filter))
    new_image=[[0 for x in range(len(im[0]))] for y in range(len(im))] 
    # ignores boundary values
    for i in range(int(len(filter)/2),len(im)-int(len(filter)/2)):
        for j in range(int(len(filter)/2),len(im[0])-int(len(filter)/2)):
            # extracts matrix for each pixel
            m = extract_matrix(i,j,im,len(filter))
            # result is the convolution
            new_image[i][j] = convolution(m,filter)
    return new_image
# sobel filter around x axis
sobel_x=[[1,0,-1],[2,0,-2],[1,0,-1]]
#sobel filter around y axis
sobel_y=[[1,2,1],[0,0,0],[-1,-2,-1]]
# reads image to perform operation in gray scale
image = cv2.imread('task1.png',0)
# converts to nested list
image_list=image.tolist()

# filter with sobel x and saves the output image
filtered_image_sobel_x=apply_filter(image_list,sobel_x)
sobel_x=numpy.asarray(filtered_image_sobel_x)
cv2.imwrite('sobel_x.png',sobel_x)

# filter with sobel y and saves the output image
filtered_image_sobel_y=apply_filter(image_list,sobel_y)
sobel_y=numpy.asarray(filtered_image_sobel_y)
cv2.imwrite('sobel_y.png',sobel_y)

