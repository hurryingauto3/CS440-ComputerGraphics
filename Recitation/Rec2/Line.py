from myimage import *
import math
def Line(img: MyImage, v1: (int, int), v2: (int,int), Color):
    v1 = list(v1)
    v2 = list(v2)
    vertices = [v1, v2]  


    vec = [v2[0]-v1[0], v2[1]-v1[1]]
    vecn = [vec[0]/(math.sqrt(vec[0]**2 + vec[1]**2)), vec[1]/(math.sqrt(vec[0]**2 + vec[1]**2))]
    i = 0
    while (v2[0]> v1[0] + i*vecn[0] or v2[1]> v1[1] + i*vecn[1]): 
        img.putpixel((int(v1[0] + i*vecn[0]), int(v1[1] + i*vecn[1])), (Color[0], Color[1], Color[2], 255))
        i+=1




