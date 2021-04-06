from myimage import *
import random
import math


def sierpinski(img: MyImage, n: int, v1: (int, int), v2: (int, int), v3: (int, int)):
    pairs = [v1, v2, v3]
    #Choose random position within the triangle
    curpos = (random.randint(min([i[0] for i in pairs]), max([i[0] for i in pairs])), 
            random.randint(min([i[1] for i in pairs]), max([i[1] for i in pairs])))
    
    for i in range(n):
        #Choose any random vertex to move towards
        randsel = random.choice(pairs)
        newpos = (curpos[0] + 0.5*(randsel[0] - curpos[0]), curpos[1] + 0.5*(randsel[1] - curpos[1])) 
        curpos = newpos

        #List of shortest distances of the curpos from each vertex
        pythagdist = [math.sqrt((i[0] - curpos[0])**2 + (i[1] - curpos[1])**2) for i in pairs]
        
        #Coloring according to closest vertex
        if pythagdist[0] == min(pythagdist):
            img.putpixel((curpos), (255,0,0,255))
        elif pythagdist[1] == min(pythagdist):
            img.putpixel((curpos), (0,255,0,255))
        else:
            img.putpixel((curpos), (0,0,255,255))

    img.show()
