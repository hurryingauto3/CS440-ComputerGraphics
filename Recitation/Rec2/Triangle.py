from Line import *

def triangle(v1: (int, int), v2: (int, int), v3: (int, int), Color, Border = None): 
    pairs = [v1, v2, v3]
    img = MyImage((1920, 1080), 0, 1)
    if Border == None:
        Line(img, v1, v2, Color)
        Line(img, v1, v3, Color)
        Line(img, v3, v2, Color)
    else:
        Line(img, v1, v2, Border)
        Line(img, v1, v3, Border)
        Line(img, v3, v2, Border)
    
    for i in range(min(i[0] for i in pairs), max(i[0] for i in pairs)):
        for j in range(min(j[1] for j in pairs), max(j[0] for j in pairs)):
            w1 = (v1[0]*(v3[1] - v1[1]) + (j - v1[1])*(v3[0] - v1[0]) - i*(v3[1] - v1[1]))/((v2[1]- v1[1])*(v3[0] - v1[0]) - (v2[0] - v1[0])*(v3[1] - v1[1]))
            w2 = (j - v1[1] - w1*(v2[1]-v1[1]))/(v3[1]-v1[1])
            if Border == None:
                if w1 >= 0 and w2 >= 0 and w1 + w2 <= 1: 
                    img.putpixel((i,j),  (Color[0], Color[1], Color[2], 255))
            else:   
                if w1 > 0 and w2 > 0 and w1 + w2 < 1:
                    img.putpixel((i,j),  (Color[0], Color[1], Color[2], 255))
        
    img.show()