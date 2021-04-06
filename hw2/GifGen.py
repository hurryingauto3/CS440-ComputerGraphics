import numpy as np
from myimage import *
import itertools
import random


def draw_line_dda(img: MyImage, v1: (int, int), v2: (int, int)):

    grad = 0
    line = np.array([])
    while True:
        try:
            grad = (v2[1]-v1[1])/(v2[0]-v1[0])
            if min(v1[0], v2[0]) == v1[0]:
                line = np.array(list((x,v1[1]+x*grad) for x in range (v1[0],v2[0])))
                break
            else:
                line = np.array(list((x,v2[1]+x*grad) for x in range (v2[0],v1[0])))
                break
        except ZeroDivisionError:
            line = np.array(list((v1[0],y) for y in range (abs(min(v1[1], v2[1])), abs(max(v1[1]+1, v2[1]+1)))))
            break
          
    [img.putpixel(i, (255, 255, 255, 255)) for i in line]
    
    # print(line)

def draw_line(img: MyImage, v1: (int, int), v2: (int, int), c1: (int, int, int, int), c2: (int, int, int, int)): 
    grad = 0
    rgb_grad = [0,0,0,0]
    line = np.array([])
    color_grad = np.array([])
    
    while True:
        try:
            grad = (v2[1]-v1[1])/(v2[0]-v1[0])
            if min(v1[0], v2[0]) == v1[0]:
                line = np.array(list((x,v1[1]+x*grad) for x in range (v1[0],v2[0])))
                break
            else:
                line = np.array(list((x,v2[1]+x*grad) for x in range (v2[0],v1[0])))
                break
        except ZeroDivisionError:
            line = np.array(list((v1[0],y) for y in range (abs(min(v1[1], v2[1])), abs(max(v1[1]+1, v2[1]+1)))))
            break
    
    while True:
        try:
            rgb_grad[1] = int((c2[1]-c1[1])/(c2[0]-c1[0]))
            rgb_grad[2] = int((c2[2]-c1[2])/(c2[0]-c1[0]))
            rgb_grad[3] = int((c2[3]-c1[3])/(c2[0]-c1[0]))

            if min(c1[0], c2[0]) == c1[0]:
                color = np.array(list((
                    r%256, 
                    (c1[1] + rgb_grad[1]*r)%256, 
                    (c1[2] + rgb_grad[2]*r)%256,
                    (c1[3] + rgb_grad[3]*r)%256) 
                    for r in range(c1[0], c2[0])))
                break
            else:
                color = np.array(list((
                    r%256, 
                    (c2[1] + rgb_grad[1]*r)%256, 
                    (c2[2] + rgb_grad[2]*r)%256,
                    (c2[3] + rgb_grad[3]*r)%256) 
                    for r in range(c2[0], c1[0])))
                break
        except ZeroDivisionError:
                break
    [img.putpixel(i, tuple(j)) for i,j in zip(line, color)]
    
def draw_polygon_dda(img: MyImage, points: tuple, colors: tuple):
    for i in range (len(points)-1):
        draw_line(img, random.choice(points), random.choice(points), colors[i], colors[i+1])


points = [(0,0),(0,100), (100,100), (100,0),(0,0),(0,100), (100,100), (100,0) ]
color = [(0,255,255,255), (255, 255, 255, 255), (0,255,255, 255), 
        (255, 255, 255, 255), (0,255,255,255), (255, 255, 255, 255),
        (0,255,255, 255), (255, 255, 255, 255)]

imgs = []
for i in range (50):
    img = MyImage((101,101 ), 0, 1)
    draw_polygon_dda(img, points, color)
    img1 = Image.new("RGB", (101,101), (0,0,0,0))
    img1.putdata(img.getdata())
    imgs.append(img1)



img = Image.new("RGB", (101,101), (0,0,0,0))
img.putdata(imgs[0].getdata())
img.save('out.gif', save_all = True, append_images = imgs[0:], optimize = False, duration= 40, loop= 0)
