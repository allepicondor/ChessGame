import PIL
from PIL import Image
import numpy as np
#https://icons8.com/upscaler
#https://imagecolorpicker.com/en/
im = Image.open('Bishop.png')
 
out = Image.new('RGBA', im.size, 0x000000)

width, height = im.size
for x in range(width):
    for y in range(height):
        r,g,b = im.getpixel((x,y))
        if (r <= 150 and r >= 60) and (g <= 200 and g >= 68)and (b <= 106 and b >= 20) and not r==g==b:
            out.putpixel((x,y), (255,255,255,0))
        else:
            out.putpixel((x,y), (r,g,b))

out.save('bar.png')