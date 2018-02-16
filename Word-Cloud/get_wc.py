import numpy as np
import sys
import jieba
from PIL import Image
import numpy as np

from wordcloud import WordCloud, STOPWORDS

if len(sys.argv) != 5:
    print('Wrong number of arguments.')
    sys.exit(0)

# Read the text.
text = open(sys.argv[1], encoding='gbk').read()

# read the mask image
im = Image.open(open(sys.argv[2], 'rb')).convert('L')
means = np.mean(im)

WHITE, BLACK = 255, 0
im = im.point(lambda x: WHITE if x > means else BLACK)
im.convert('1')

mask = np.array(im)

wc = WordCloud(background_color="white", max_words=2000, mask=mask, font_path=sys.argv[3])
 
# generate word cloud
wc.generate(" ".join(jieba.cut(text)))

# store to file
wc.to_file(sys.argv[4])

