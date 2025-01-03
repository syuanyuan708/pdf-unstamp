#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rgb相关操作
"""

import os
import unittest
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class TestRGB(unittest.TestCase):

    # 图片转为bmp格式
    def test_pic2bmp(self):
        # 打开图片文件
        inputFileName = "image/lena.jpeg"
        img = Image.open(inputFileName)

        # jpeg 格式转为无压缩 bmp 格式
        outputFileName = str.replace(inputFileName, ".jpeg", ".bmp")
        img.save(outputFileName)

    
    # 分离rgb通道
    def test_split_rgb(self):
        # 读取图像
        image = cv2.imread("image/lena.jpeg")

        # 创建窗口
        cv2.namedWindow("R", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        cv2.namedWindow("B", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        cv2.namedWindow("G", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

        # 通道拆分
        r = image.copy()
        r[:, :, [0, 1]] = 0

        b = image.copy()
        b[:, :, [1, 2]] = 0

        g = image.copy()
        g[:, :, [0, 2]] = 0

        # 水平拼接
        hmerge = np.hstack((r, b, g))

        # 显示图像
        cv2.imshow("R-B-G", hmerge)

        key = chr(cv2.waitKey())
        if key == "1":
            print("图像显示结束")
            cv2.destroyAllWindows()

    
    # 获取图片rgb值
    def test_get_rgb(self):
        # 读取图片
        image = cv2.imread('pdf/mobile.jpeg')

        # 获取图片的RGB值
        rgb_values = image[:, :, ::-1]

        # 显示图片
        plt.imshow(rgb_values)
        plt.axis('off')
        plt.show()
        print()


if __name__ == "__main__":
    unittest.main()
