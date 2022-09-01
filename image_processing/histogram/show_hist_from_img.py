# -*- encoding: utf-8 -*-
"""
@File Name      :   show_hist_from_img.py
@Create Time    :   2022/9/1 15:33
@Description    :   
@Version        :   
@License        :   MIT
@Author         :   diklios
@Contact Email  :   diklios5768@gmail.com
@Github         :   https://github.com/diklios5768
@Blog           :   
@Motto          :   All our science, measured against reality, is primitive and childlike - and yet it is the most precious thing we have.
"""
__auth__ = 'diklios'

import click
import cv2
from matplotlib import pyplot as plt


@click.command()
@click.argument('image_path', type=click.Path(exists=True))
def main(image_path):
    img = cv2.imread(image_path)
    img_red = img[:, :, 2]
    img_green = img[:, :, 1]
    img_blue = img[:, :, 0]

    hist_red = cv2.calcHist([img_red], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([img_green], [0], None, [256], [0, 256])
    hist_blue = cv2.calcHist([img_blue], [0], None, [256], [0, 256])
    plt.plot(hist_red, color='red')
    plt.plot(hist_green, color='green')
    plt.plot(hist_blue, color='blue')
    plt.xlim([0, 256])
    plt.title("image2")
    plt.show()


if __name__ == '__main__':
    """
    从图片展示直方图
    """
    main()
