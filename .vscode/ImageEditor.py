import Image
im = Image.open("PiecesImg/White/pawn.png")   
out = Image.new('I', im.size, 0xffffff)

width, height = im.size
for x in range(width):
    for y in range(height):
        r,g,b = im.getpixel((x,y))
        if b < g and b < r or r==g==b:
            out.putpixel((x,y), 0)

out.save('bar.png')