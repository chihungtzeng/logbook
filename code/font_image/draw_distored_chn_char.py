# -*- coding: utf-8 -*-
"""
Draw a single char in png/jpeg formats. The output can be used for machine
learning.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
__SIZE = 24


def main():
    """ Prog entry """
    # RGB mode, with with background
    image = Image.new("RGB", (__SIZE, __SIZE), color="rgb(255, 255, 255)")
    # initialise the drawing context
    draw = ImageDraw.Draw(image)
    # Remember to cp odosung.ttc to the directory where this script locates.
    font = ImageFont.truetype('odosung.ttc', size=__SIZE)
    # draw the message on the background
    draw.text((0, 0), u"王", fill="rgb(0, 0, 0)", font=font)
    image = image.filter(ImageFilter.GaussianBlur(2))
    # save the edited image
    image.save('wang.png')

if __name__ == "__main__":
    main()
