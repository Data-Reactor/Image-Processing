def get_char(pixel):
    if 0 <= pixel < 25.5:
        return '@'
    elif 25.5 <= pixel < 25.5 * 2:
        return '#'
    elif 25.5 * 2 <= pixel < 25.5 * 3:
        return '%'
    elif 25.5 * 3 <= pixel < 25.5 * 4:
        return '&'
    elif 25.5 * 4 <= pixel < 25.5 * 5:
        return '$'
    elif 25.5 * 5 <= pixel < 25.5 * 6:
        return '*'
    elif 25.5 * 6 <= pixel < 25.5 * 7:
        return '+'
    elif 25.5 * 7 <= pixel < 25.5 * 8:
        return '-'
    elif 25.5 * 8 <= pixel < 25.5 * 9:
        return '.'
    else:
        return ' '

from PIL import Image
import numpy as np

im = Image.open('test.jpg').convert('L')
width_new = 65
rows, cols = im.size

height_new = int(cols * width_new / rows)
im = im.resize((width_new, height_new))

text = ''
im = np.array(im)

rows, cols = im.shape
for i in range(rows):
    for j in range(cols):
        char = get_char(im[i, j])
        text += char
    text += '\n'

print(text)

