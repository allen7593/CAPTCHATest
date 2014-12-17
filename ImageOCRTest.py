__author__ = 'Allen_Guest'

from PIL import Image
import pytesser
sizex = 20
sizey = 58
file_o = open("result.txt", 'a')
for i in range(50):
    im = Image.open("vCode%d.png" % i)
    im = im.convert("RGBA")
    pixdata = im.load()
    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)

    #box = (0,0,sizey,sizex)
    box = (2, 2, sizey-2, sizex-2)
    region = im.crop(box)

    region.save("input-black.jpg", "jpeg")

    im_orig = Image.open('input-black.jpg')
    #big = im_orig.resize((540, 160), Image.NEAREST)
    #big.show()
    #big.save("test.bmp")

    file_o.write(pytesser.image_to_string(im_orig))
file_o.close()
"""
imageSize = (20, 58)
image = Image.frombytes('RGB', imageSize, rawData, "F;16")
image.save("foo.png")
"""
