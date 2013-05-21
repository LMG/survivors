#!/usr/bin/python2
# coding=utf8

import numpy as np
import cv2
import cv2.cv as cv

angleDeChamp = 47 #angle de champ habituel pour les appareils photo, à vérifier (en degrés)
tailleBalle = 5 #taille en cm bidon

#load image
im = cv2.imread('res/testBalle.png')
cv2.imshow('window1',im)

#get circle diameter
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
imDst = cv2.inRange(imgray,cv.Scalar(20,100,100),cv.Scalar(20,255,255))
imDstContours = cv2.findContours(imDst, cv.CV_RETR_EXTERNAL, cv.CV_CHAIN_APPROX_NONE)
#imDstPlus = zeros(cv2.inputFrame.size(), cv2.inputFrame.type())
#cv2.drawContours(imDstPlus, imDstContours, -1, cv.Scalar(255,0,0), cv.CV_FILLED)

#compute distance

#display stuff
cv2.namedWindow('window1',cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow('window2',cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow('window3',cv2.CV_WINDOW_AUTOSIZE)

cv2.imshow('window1',imDst)
cv2.imshow('window2',im)
cv2.imshow('window3',imgray)
cv2.waitKey(100000)

