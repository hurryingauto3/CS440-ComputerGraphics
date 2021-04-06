from myimage import *
import random
import math

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

def resize(img):
    img = MyImage.open(img)

    img1 = MyImage((img.size[0] * 2, img.size[1] * 2), 0, 1,'RGBA')

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            img1.putpixel((x*2, y*2), img.getpixel((x, y)))

            pix1 = img.getpixel((x, y))
            if x != img.size[0] - 1:
                # pix1 and pix2 are neighbouring pixels in the original image with the same row
                pix2 = img.getpixel((x + 1, y))
                avgP = ((pix1[0] + pix2[0]) // 2,
                        (pix1[1] + pix2[1]) // 2,
                        (pix1[2] + pix2[2]) // 2,
                        (pix1[3] + pix2[3]) // 2)

                img1.putpixel((x * 2 + 1, y * 2), avgP)

            if y != img.size[1] - 1:
                # pix1 and pix3 are neighbouring pixels in the original image with the same column
                pix3 = img.getpixel((x, y + 1))

                avgQ = ((pix1[0] + pix3[0]) // 2,
                        (pix1[1] + pix3[1]) // 2,
                        (pix1[2] + pix3[2]) // 2,
                        (pix1[3] + pix3[3]) // 2)

                img1.putpixel((x * 2, y * 2 + 1), avgQ)

            if y != img.size[1] - 1 and x != img.size[0] - 1:
                # pix4 is to pix1's immediate bottom right in the original image
                pix2 = img.getpixel((x + 1, y))
                pix3 = img.getpixel((x, y + 1))
                pix4 = img.getpixel((x + 1, y + 1))

                avgR = ((pix1[0] + pix2[0] + pix3[0] + pix4[0]) // 4,
                        (pix1[1] + pix2[1] + pix3[1] + pix4[1]) // 4,
                        (pix1[2] + pix2[2] + pix3[2] + pix4[2]) // 4,
                        (pix1[3] + pix2[3] + pix3[3] + pix4[3]) // 4)

                img1.putpixel((x * 2 + 1, y * 2 + 1), avgR)
                
    for y in range(img1.size[1]):
        for x in range(img1.size[0]):
            if x == img1.size[0] - 1:
                if y % 2 == 0:
                    img1.putpixel((x, y), img1.getpixel((x-1, y)))  # copy rgb of pixel to the left
                else:
                    pixAbove = img1.getpixel((x, y - 1))  # rgb of pixel above
                    pixLeft = img1.getpixel((x-1, y))  # rgb of pixel to the left

                    pixBound = ((pixAbove[0] + pixLeft[0]) // 2,
                                (pixAbove[1] + pixLeft[1]) // 2,
                                (pixAbove[2] + pixLeft[2]) // 2,
                                (pixAbove[3] + pixLeft[3]) // 2)
                    img1.putpixel((x, y), pixBound)

            elif y == img1.size[1] - 1:
                if x % 2 == 0:
                    img1.putpixel((x, y), img1.getpixel((x, y-1)))  # copy rgb of pixel above
                else:
                    pixAbove = img1.getpixel((x, y - 1))  # rgb of pixel above
                    pixLeft = img1.getpixel((x-1, y))  # rgb of pixel to the left

                    pixBound = ((pixAbove[0] + pixLeft[0]) // 2,
                                (pixAbove[1] + pixLeft[1]) // 2,
                                (pixAbove[2] + pixLeft[2]) // 2,
                                (pixAbove[3] + pixLeft[3]) // 2)
                    img1.putpixel((x, y), pixBound)


    img.show()
    img1.show()

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
