import numpy as np
from myimage import *
from api import *
import itertools
import math
import colorsys

def drawNthSierpinski(n: int, height: int, startPoint: tuple, img: MyImage):
    width = height
    bottomLeftP = startPoint  # bottom left point
    topPoint = (startPoint[0] + width // 2, startPoint[1] - height)  # topmost point
    bottomRightP = (startPoint[0] + width, startPoint[1])  # Bottom Right point

    HighTriStart = (startPoint[0] + width // 4, startPoint[1] - height//2)  # starting point for highest sierpinski
    RightTriStart = (startPoint[0] + width // 2, startPoint[1])  # starting point for rightmost sierpinski

    if n == 0:
        # Drawing basic triangle
        draw_line_dda(img, bottomLeftP, topPoint)
        draw_line_dda(img, topPoint, bottomRightP)
        draw_line_dda(img, bottomRightP, bottomLeftP)

    else:
        # Drawing 3 triangles with n-1 recursive depth and a height that is half of the original
        drawNthSierpinski(n - 1, height // 2, bottomLeftP, img)
        drawNthSierpinski(n - 1, height // 2, HighTriStart, img)
        drawNthSierpinski(n - 1, height // 2, RightTriStart, img)

def sierpinski(recursive_depth: int):
    height = 100
    width = height
    # myImgWidth = width * (recursive_depth+1)
    # myImgHeight = height
    myImgWidth = (width + 1) * (recursive_depth+1) - (recursive_depth + 1)
    myImgHeight = height + 1
    initialPoint = (0, height)  # Starting point for leftmost triangle
    img1 = MyImage((myImgWidth, myImgHeight), 5, 10)  # grid and pixel size chosen arbitrarily
    for i in range(recursive_depth+1):
        drawNthSierpinski(i, height, initialPoint, img1)
        initialPoint = (initialPoint[0] + width, height)

    img1.show()

def midpoint_finder(center, point, rad):

    """Finds the extact coordinate of the new 
    mid point between two vertices that is also 
    1 radius length away from the center"""

    vec = [
        point[0] - center[0], 
        point[1] - center[1]
    ]
    vec_len = math.sqrt(vec[0]**2 + vec[1]**2)
    unit_vec = [vec[0]/vec_len, vec[1]/vec_len]
    return (int(center[0]+ rad*unit_vec[0]), int(center[1]+ rad*unit_vec[1]))

def shift_point(point, rad):
    """Shift any coordinate horizontally by a distance of rad"""
    return (point[0] + rad, point[1])

def circle(rad: int, subdiv: int):
    images = []
    center = (rad, rad)
    
    #Defines the coordinates of the base circle, with 0 subdivisions
    points = [(center[0], center[1] - rad),
            (center[0]+ rad, center[1]),
            (center[0], center[1] + rad),
            (center[0] - rad, center[1] )]
    color = [(255, 0, 0, 255) for i in range(4)]

    if subdiv == 0:
        img = MyImage((2*rad + 1, 2*rad+1, 0, 1))
    else:
        #The width of the image will be determined on the number of circles required
        img = MyImage((2*(subdiv+1)*rad+1, 2*rad+1), 0, 1)
    
    img.fill((255,255,255,255))
    #Prints the diamond circle
    draw_polygon_dda(img, points, color)

    for i in range(subdiv):
        midpoints = []
        points_shifted = []
        points_new = []
        for j in range (len(points)-1):
            #The mid point finder function finds the midpoints between each coordinate in the circle
            midpoints.append(midpoint_finder(center, ((points[j][0] + points[j+1][0])//2,
                        (points[j][1]  + points[j+1][1])//2), rad))       
            color.append((255, 0, 0, 255))

        #The midpoint is found between the last coordinate and the first coordinate
        midpoints.append(midpoint_finder(center, ((points[-1][0] + points[0][0])//2,
                        (points[-1][1]  + points[0][1])//2), rad))
        color.append((255,0,0, 255))
        
        #Stitches the list of midpoints and the points of the old circle together
        for f in range (len(points)):
            points_new.append(points[f])
            points_new.append((midpoints[f]))

        #The old circles coordinates are replaced with the new circles coordinates
        points = points_new
        #Shifts all the points of the new circle to its new position relative to the first circle
        points_shifted = [shift_point(x, (i+1)*2*rad) for x in points_new]
        draw_polygon_dda(img, points_shifted, color)
        images.append(img)
        
    img.show()
    return img
    
def map_point(P, Q, A, B, X):
    if len(A) == 4:  # Using the lines list returned by draw_line() when A and B are color tuples
        width = max(P[0], Q[0]) + 10  # To ensure image is greater than line
        height = max(P[1], Q[1]) + 10
        imgMap = MyImage((width, height), 5, 10)
        pixColors = draw_line(imgMap, (P, A), (Q, B))
        for i in pixColors:
            if i[0][0] == X[0] and i[0][1] == X[1]:
                return i[1]
    else:  # For all other cases. Works without the if above but I felt it could've been less accurate
        totDist = math.sqrt(((P[0] - Q[0])**2) + ((P[1] - Q[1])**2))  # Dist between original points
        XDist = math.sqrt(((P[0] - X[0])**2) + ((P[1] - X[1])**2))  # Dist between P and X
        alpha = XDist/totDist  # Ratio between the two variables calculated above
        lst = []
        for i in range(len(A)):
            diff = B[i] - A[i]  # Calculate diff between corresponding values of B and A
            lst.append(A[i] + int(diff * alpha))  # Calculate corresponding mapping of X using value of A and the increment from alpha*diff.
        return lst



def mandelbrot_iter(c, rec_depth):  # Used to calculate escape time of c
    z = 0
    n = 0
    while abs(z) <= 2 and n < rec_depth:
        if n == rec_depth:
            return rec_depth  # Return recursion depth if escape time is greater than recursion depth
        z = z*z + c  # Calculate next z value
        n += 1
    return n

def mandelbrot(rec_depth: int):
    dim = (200, 200)
    img = Image.new("HSV", dim)
    RE_START = -2  # Defining range of complex co-ordinate frame
    RE_END = 2
    IM_START = -2
    IM_END = 2

    for i in range(dim[0]):
        for j in range(dim[1]):
            c = complex(RE_START + (i/dim[0])*(RE_END - RE_START),
                        IM_START + (j/dim[1])*(IM_END - IM_START))  # Calculating complex value of point

            m = mandelbrot_iter(c, rec_depth)  # Finding escape time of above complex value
            
            hue = int(255 * m / rec_depth)  # Calculating HSV color value
            saturation = 255
            value = 255 if m < rec_depth else 0

            img.putpixel((i, j), (hue, saturation, value))  # Coloring pixels
    
    img.show()
    
    
def testingApp():
    # sierpinski(5)
    mandelbrot(100)


# testingApp()
