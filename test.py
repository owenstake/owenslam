#!/usr/bin/python3.8
import time
import cv2
import pygame
import sdl2.ext
import numpy as np
from extractor import Extractor
from display import Display
from display import Display2D

W = 1920//2
H = 1080//2

# disp = Display2D(W, H)
disp = Display(W, H)
fe = Extractor()

def process_frame(img):
    img = cv2.resize(img, (W,H))
    matches = fe.extract(img)
    print(dir(matches))

    for pt1, pt2 in matches:
        print("pt1")
        print(dir(pt1))
        # print(pt2)
        # cv2.circle(img, (int(round(pt1.pt[0])), int(round(pt1.pt[1]))), color=(0,255,0), radius=3)
        # u1 = int(round(pt1.pt[0]))
        # v1 = int(round(pt1.pt[1]))
        # u2 = int(round(pt2.pt[0]))
        # v2 = int(round(pt2.pt[1]))
        # u1,v1 = pt1
        # u2,v2 = pt2
        u1,v1 = map(lambda x: int(round(x)), pt1)
        u2,v2 = map(lambda x: int(round(x)), pt2)
        cv2.circle(img, (u1, v1), color=(0,255,0), radius=3)
        cv2.line(img, (u1,v1), (u2,v2), color=(255,0,0))

    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("./test_countryroad.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break

