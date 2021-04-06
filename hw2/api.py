import numpy as np
from myimage import *
import itertools

def draw_line_dda(img: MyImage, v1: (int, int), v2: (int, int)):

    grad = 0
    line = np.array([])
    while True:
        try:
            grad = (v2[1]-v1[1])/(v2[0]-v1[0])  # y2 - y1/ x2 - x1 for gradient calculation
            # For grad > 1, the line is drawn in terms of y
            if abs(grad) <= 1:
                # Grad is absolute, points are interchanged depending on the larger x-value
                if min(v1[0], v2[0]) == v1[0]:
                    # Creates an array line that contains all points from v1 to v2. Made using increments in y value
                    line = np.array(list((x, int(v1[1] + ((x - v1[0]) * grad))) for x in range(v1[0], v2[0] + 1)))
                    break
                else:
                    # Creates an array line that contains all points from v2 to v1. Made using increments in y value
                    line = np.array(list((x, int(v2[1] + ((x - v2[0]) * grad))) for x in range (v2[0], v1[0] + 1)))
                    break
            else:
                # Grad is absolute, points are interchanged depending on the larger y-value
                if min(v1[1], v2[1]) == v1[1]:
                    # Creates an array line that contains all points from v1 to v2. Made using increments in x value
                    line = np.array(list((int(v1[0] + ((y - v1[1]) * (1 / grad))), y) for y in range(v1[1], v2[1] + 1)))
                    break
                else:
                    # Creates an array line that contains all points from v2 to v1. Made using increments in x value
                    line = np.array(list((int(v2[0] + ((y - v2[1]) * (1/grad))), y) for y in range (v2[1], v1[1] + 1)))
                    break

        # For when x values don't change
        except ZeroDivisionError:
            line = np.array(list((v1[0],y) for y in range (abs(min(v1[1], v2[1])), abs(max(v1[1]+1, v2[1]+1)))))
            break
    # White colored line is put on the image.
    [img.putpixel(i, (255, 255, 255, 255)) for i in line]    
    
def draw_line(img: MyImage, v1: ((int, int), (int, int, int, int)), v2: ((int, int), (int, int, int, int))):

    c1 = np.array(v1[1])  # Color of point 1
    c2 = np.array(v2[1])  # Color of point 2
    color_diff = c2 - c1  # Color difference between the two
    grad = 0
    
    line = np.array([])
    color = np.array([])
    
    while True:
        try:
            grad = (v2[0][1] - v1[0][1]) / (v2[0][0] - v1[0][0])  # y2 - y1/ x2 - x1 for gradient calculation
            #  For grad > 1, the line is drawn in terms of y
            if abs(grad) <= 1:
                color_grad = color_diff / (v2[0][0] - v1[0][0])
                # Grad is absolute, points are interchanged depending on the larger x-value
                if min(v1[0][0], v2[0][0]) == v1[0][0]:
                    # Creates an array line that contains all points from v1 to v2. Made using increments in y value
                    line = np.array(list((x, int(v1[0][1] + ((x - v1[0][0]) * grad))) for x in range(v1[0][0],v2[0][0] + 1)))
                    color = np.array(list((
                        int(c1[0]+color_grad[0]*x)%256, # Creating an array that contains gradually changing color value based on gradient.
                        int(c1[1]+color_grad[1]*x)%256,
                        int(c1[2]+color_grad[2]*x)%256,
                        int(c1[3]+color_grad[3]*x)%256)
                        for x in range(v2[0][0] - v1[0][0] + 1)))
                    break

                else:
                    # Creates an array line that contains all points from v2 to v1. Made using increments in y value
                    line = np.array(
                        list((x, int(v2[0][1] + ((x - v2[0][0]) * grad))) for x in range(v2[0][0], v1[0][0] + 1)))
                    color = np.array(list((
                        int(c2[0]+color_grad[0]*x)%256,  # Creating an array that contains gradually changing color value based on gradient.
                        int(c2[1]+color_grad[1]*x)%256,
                        int(c2[2]+color_grad[2]*x)%256,
                        int(c2[3]+color_grad[3]*x)%256)
                        for x in range(v1[0][0] - v2[0][0] + 1)))
                    break
            else:
                color_grad = color_diff / (v2[0][1] - v1[0][1])
                # Grad is absolute, points are interchanged depending on the larger y-value
                if min(v1[0][1], v2[0][1]) == v1[0][1]:
                    # Creates an array line that contains all points from v1 to v2. Made using increments in x value
                    line = np.array(list((int(v1[0][0] + ((y - v1[0][1]) * (1 / grad))), y) for y in range(v1[0][1], v2[0][1] + 1)))
                    color = np.array(list((
                        int(c1[0]+color_grad[0]*y)%256,  # Creating an array that contains gradually changing color value based on gradient.
                        int(c1[1]+color_grad[1]*y)%256,
                        int(c1[2]+color_grad[2]*y)%256,
                        int(c1[3]+color_grad[3]*y)%256)
                        for y in range(v2[0][1] - v1[0][1] + 1)))
                    break
                else:
                    # Creates an array line that contains all points from v2 to v1. Made using increments in x value
                    line = np.array(
                        list((int(v2[0][0] + ((y - v2[0][1]) * (1 / grad))), y) for y in range(v2[0][1], v1[0][1] + 1)))
                    color = np.array(list((
                        int(c2[0]+color_grad[0]*y)%256,  # Creating an array that contains gradually changing color value based on gradient.
                        int(c2[1]+color_grad[1]*y)%256,
                        int(c2[2]+color_grad[2]*y)%256,
                        int(c2[3]+color_grad[3]*y)%256)
                        for y in range(v1[0][1] - v2[0][1] + 1)))
                    break
        # For when x values don't change
        except ZeroDivisionError:
            color_grad = color_diff / (v2[0][1] - v1[0][1])
            if min(v1[0][1], v2[0][1]) == v1[0][1]:
                line = np.array(list((v1[0][0],y) for y in range (v1[0][1], v2[0][1] + 1)))
                color = np.array(list((
                            int(c1[0]+color_grad[0]*y)%256,  # Creating an array that contains gradually changing color value based on gradient.
                            int(c1[1]+color_grad[1]*y)%256,
                            int(c1[2]+color_grad[2]*y)%256,
                            int(c1[3]+color_grad[3]*y)%256)
                            for y in range(v2[0][1] - v1[0][1] + 1)))
                
            else:
                line = np.array(list((v1[0][0],y) for y in range (v2[0][1], v1[0][1] + 1)))
                color = np.array(list((
                        int(c2[0]+color_grad[0]*y)%256,  # Creating an array that contains gradually changing color value based on gradient.
                        int(c2[1]+color_grad[1]*y)%256,
                        int(c2[2]+color_grad[2]*y)%256,
                        int(c2[3]+color_grad[3]*y)%256)
                        for y in range(v1[0][1] - v2[0][1] + 1)))
            break


    [img.putpixel(i, tuple(j)) for i,j in zip(line, color)]
    return [(i, tuple(j)) for i,j in zip(line, color)]
    
    
def draw_polygon_dda(img: MyImage, points: tuple, colors: tuple):
    try:
        for i in range (len(points)-1):
            draw_line(img, (points[i], colors[i]), (points[i+1], colors[i+1]))  # Drawing lines between successive vertices
        draw_line(img, (points[-1], colors[-1]), (points[0],colors[0]))  # Drawing a line between the last and first vertices

    except TypeError:  # for when n=1
        img.putpixel(points, colors)

def draw_polygon(img: MyImage, points: tuple, colors: tuple, fill = True):
    draw_polygon_dda(img, points, colors)  # Drawing boundary lines
    if fill:
        savedPixelColors = []
        try:  # lines 145 - 151 are the same as draw_polygon_dda except boundary pixels and colors are appended to a list.
            for i in range(len(points) - 1):
                savedPixelColors.extend(draw_line(img, (points[i], colors[i]),
                          (points[i + 1], colors[i + 1]))) # Drawing lines between successive vertices

            if len(points) > 2:
                savedPixelColors.extend(draw_line(img, (points[-1], colors[-1]),
                        (points[0], colors[0])))  # Drawing a line between the last and first vertices

        except TypeError:  # for when n=1
            img.putpixel(points, colors)

        for i in savedPixelColors:  # Iterating over list containing boundary pixels and color pairs
            pixel = i[0]
            pixelColor = i[1]
            pixelYVal = i[0][1]
            pixelXVal = i[0][0]
            try:
                for j in savedPixelColors:
                    if pixelYVal == j[0][1] and pixelXVal != j[0][0]:  # Condition checks for a different boundary point that in the same row
                        draw_line(img, (pixel, pixelColor), (j[0], j[1]))  # Draw a line between the two points
            except:
                pass


def apiTest():
    print("testing")
    img = MyImage((200, 200), 5, 10)
    # draw_line_dda(img, (20,150), (70, 50))
    # draw_line_dda(img, (70,50), (120, 150))
    # draw_line_dda(img, (120,150), (20, 150))
    # draw_line_dda(img, (10,50), (5, 100))
    # print(draw_line(img, ((50, 80), (255, 0, 0, 255)), ((80, 50), (0, 255, 0, 255))))
    # draw_line(img, ((80, 50), (255, 0, 0, 255)), ((50, 80), (0, 255, 0, 255)))
    # draw_line(img, ((100, 50), (255, 0, 0, 255)), ((50, 50), (0, 255, 0, 255)))
    # draw_line(img, ((100, 50), (0, 255, 0, 255)), ((50, 50), (255, 0, 0, 255)))
    # draw_line(img, ((100, 50), (0, 255, 0, 255)), ((100, 100), (255, 0, 0, 255)))
    # draw_line(img, ((100, 100), (0, 255, 0, 255)), ((100, 50), (255, 0, 0, 255)))
    points = ((50,100), (100, 0), (150, 100))
    color = ((255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255))
    # points = ((0, 0), (50,0), (50, 100), (0, 100))
    # color = ((255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255), (255, 255, 255, 255))
    # points = ((0,0),(0,100), (100,100), (100,0))
    # color = ((255,0,0,255), (0, 255, 0, 255), (0,0,255, 255), (255, 255, 255, 255))

    draw_polygon_dda(img, points, color)
    # draw_polygon(img, points, color)

    img.show()

# apiTest()
