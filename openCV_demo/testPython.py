#!/usr/bin/python2

import numpy as np
import cv2


cv2.namedWindow('window1',cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow('window2',cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow('window3',cv2.CV_WINDOW_AUTOSIZE)
im = cv2.imread('res/image.png')
cv2.imshow('window1',im)

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,100,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im,contours,-1,(0,255,0),3)
cv2.imshow('window2',im)
cv2.drawContours(imgray,contours,-1,(0,255,0),3)
cv2.imshow('window3',imgray)
cv2.waitKey(100000)



