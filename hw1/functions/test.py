from myimage import *
from Blow import *
from Resize import *
from Sierpinski import *
# img.blow("images\logo.png")
# blow("images/logo.png")

# resize("images/sierpinski.png")

img = MyImage((500, 500), 0, 1)
sierpinski(img, 1000000, (500,0), (0,500), (500,500))
# sierpinski(img, 10000, (0,0), (500,0), (0,500))
