'''
Hex color codes work within 15 characters, 0-9 and a-f.
RGB goes into hex color codes as such # (red) 00 (green) 00 (blue) 00
Hex color codes work by rolling over the value of 09 to 0a. Once 0f
is hit (15) the following (16) would be represented as 10 instead of
(16). This means that RGB values (16, 32, 161) would evalueate to
#1020a1 (10, 20, a1)
'''

def hexgen(r, g, b):

    red = str(hex(r))
    green = str(hex(g))
    blue = str(hex(b))
    RGB = "#" + red[2:] + green[2:] + blue[2:]
    return RGB

print(hexgen(int(input()), int(input()), int(input())))