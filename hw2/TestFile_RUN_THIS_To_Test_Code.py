from application import *

def APITest():
    print("testing")
    img = MyImage((200, 200), 5, 10)

    points = ((50,100), (100, 0), (150, 100))
    color = ((255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255))
    draw_polygon_dda(img, points, color)
    img.show()
    # draw_polygon(img, points, color, True)
    # img.show()

APITest()
    
circle(50, 4)
circle(100, 5)
circle(200, 6)

mandelbrot(50)
mandelbrot(100)
mandelbrot(500)

