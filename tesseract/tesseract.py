# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/16 8:30'

# coding:utf-8

# 引入机器学习模块
import pytesseract
# 引入图形处理模块
from PIL import Image

# 引入一张图片
img = Image.open("aa.png")
# img.load()
# img.show()
# 识别图片
text = pytesseract.image_to_string(img)

print text