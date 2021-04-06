from myimage import *

def blow(img: str):

    img = MyImage.open(img)

    #declare 5 MyImage objects
    img1 = MyImage(img.size, 1, 2)
    img2 = MyImage(img.size, 1, 2)
    img3 = MyImage(img.size, 1, 2)
    img4 = MyImage(img.size, 1, 2)
    img5 = MyImage(img.size, 1, 2, mode = "CMYK")

    #Copy all of the custom images contents to MyImage object
    img1.putdata(img.getdata())
    img2.putdata([(r,0,0,a) for r,g,b,a in img1.getdata()])
    img3.putdata([(0,g,0,a) for r,g,b,a in img1.getdata()])
    img4.putdata([(0,0,b,a) for r,g,b,a in img1.getdata()])
    img5.putdata([(r,g,b,1-max((r,g,b))) for r,g,b,a in img1.getdata()])
    
    #Show all images
    img1.show()
    img2.show()
    img3.show()
    img4.show()
    img5.show()


