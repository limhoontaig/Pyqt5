from wordcloud import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

text = "IT 컴퓨터 PHP 육아 결혼 폼메일"

cat_mask = np.array(Image.open('cat.PNG'))

wordcloud = WordCloud(font_path='c:\\Windows\\Fonts\\NanumGothic.ttf', background_color = 'white', max_font_size=100,mask=cat_mask).generate(text)

plt.imshow(wordcloud,interploation='bilinear')
plt.axis('off')
plt.show()
plt.savefig('wordcloud.png')