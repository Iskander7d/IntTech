from PIL import Image
import numpy as np
from math import sqrt
from random import choice

def clear_array(array):
    #print(array.shape)
    height, width, depth = array.shape
    clear_array = []
    for i in range(height):
        empty_pixels = []
        for j in range(width):
            pixel = array[i][j]
            if len(set(pixel)) == 1:
                empty_pixels.append(pixel)
        if len(empty_pixels) != width:
            clear_array.append(array[i])

    clear_array = np.array(clear_array)
    return clear_array

def recognize_shape(array):
    shapes = {
        0 : 'h_line',
        1 : 'v_line',
        2 : 'i_line',
        3 : 'c_line',
        4 : 'triangle',
        5 : 'rect triangle',
        6 : 'isosceles triangle',
        7 : 'equilateral triangle',
        8 : 'rectangle',
        9 : 'square',
        10 : 'ellipse',
        11 : 'circle'
    }

    def rectangle():
        if height == width:
            return shapes[9]
        return shapes[8]

    def triangle():
        if width % 2 == 0:
            return None
        for j in range(width):
            pixel = array[height-1][j]
            if len(set(pixel)) == 1:
                if j == (round(width) / 2 + 1):
                    if (abs(height - width * (sqrt(3)/2)) < 0.5):
                        return shapes[7]
                    return shapes[6]
        return shapes[4]

    def ellipse():
        if height == width:
            return shapes[11]
        return shapes[10]

    height, width, depth = array.shape
    corners = [
        set(array[0][0]),
        set(array[0][width-1]),
        set(array[height-1][0]),
        set(array[height-1][width-1])
    ]

    points = []

    count = 0
    for c in corners:
        if len(c) > 1:
            points.append(count)
            count += 1

    if count == 4:
        if width == 1:
            return shapes[0]
        if height == 1:
            return shapes[1]
        return rectangle()

    if count == 3:
        return shapes[5]

    if count == 2:
        if (len(corners[0]) > 1 and len(corners[3]) > 1)\
                or (len(corners[1]) > 1 and len(corners[2]) > 1):
            return shapes[2]
        return triangle()

    if count == 0:
        return ellipse()

    else:
        return 'unrecognized shape'



def main():

    figures = [
        'v_line.bmp',
        'h_line.bmp',
        'i_line.bmp',
        'triangle.bmp',
        'rect_triangle.bmp',
        'isos_triangle.bmp',
        #'equilateral_triangle.bmp',
        'rectangle.bmp',
        'square.bmp',
        'ellipse.bmp',
        'circle.bmp'
    ]

    for f in figures:
        image = Image.open(f)
        image.load()
        array = np.array(image)
        clear_w = clear_array(array)
        clear_w = [x for x in zip(*clear_w)]
        clear_w = np.array(clear_w)
        clear_wh = clear_array(clear_w)
        shape = recognize_shape(clear_wh)
        print(shape)

if __name__ == '__main__':
    main()

