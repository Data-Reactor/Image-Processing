import numpy as np
import sys
from PIL import Image

if len(sys.argv) != 4:
    print('Wrong number of arguments.')
    sys.exit(0)

im = Image.open(open(sys.argv[1], 'rb'))
L_im = im.convert('L')
means = np.mean(L_im)
new_im = []

if sys.argv[2] == '0':
    pixel1 = [0, 0, 0]
    pixel2 = [1, 1, 1]
else:
    pixel1 = [1, 1, 1]
    pixel2 = [0, 0, 0]

for i in np.array(L_im).flat:
    if i > means:
        new_im.append(pixel1)
    else:
        new_im.append(pixel2)

new_im = np.array(new_im).reshape(np.array(im).shape)
out_im = new_im * np.array(im)
out_im = np.uint8(out_im)
Image.fromarray(out_im).save(sys.argv[3])

