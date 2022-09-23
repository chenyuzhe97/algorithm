# -*- encoding: utf-8 -*-
"""
@File Name      :   normalization.py
@Create Time    :   2022/9/23 11:32
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

import os

import click
import cv2
import numpy as np


def hist_normalized(image, gray_min: int = 0, gray_max: int = 255):
    i_min = np.min(image)
    i_max = np.max(image)
    rows, cols = image.shape
    # 输出图像
    output_image = np.zeros(image.shape, np.float32)
    # 输出图像的映射
    coefficient = float(gray_max - gray_min) / float(i_max - i_min)
    for r in range(rows):
        for c in range(cols):
            output_image[r][c] = coefficient * (image[r][c] - i_min) + gray_min
    return output_image


@click.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('--gray_min', default=0, type=int)
@click.option('--gray_max', default=255, type=int)
@click.option('--red_min', default=0, type=int)
@click.option('--red_max', default=255, type=int)
@click.option('--green_min', default=0, type=int)
@click.option('--green_max', default=255, type=int)
@click.option('--blue_min', default=0, type=int)
@click.option('--blue_max', default=255, type=int)
def main(image_path, gray_min, gray_max, red_min, red_max, green_min, green_max, blue_min, blue_max):
    image_name = os.path.basename(image_path)
    dir_path = os.path.dirname(image_path)
    # 原图

    # 直⽅图正规化
    if gray_min and gray_max:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        hist_normalized_image = hist_normalized(image, gray_min, gray_max)
        # 数据类型转换，灰度级显⽰
        hist_normalized_image = np.round(hist_normalized_image)
        hist_normalized_image = hist_normalized_image.astype(np.uint8)
        # 保存图像
        hist_normalized_image_name = f"hist_normalized-gray-{gray_min}-{gray_max}-{image_name}"
        cv2.imwrite(os.path.join(dir_path, hist_normalized_image_name), hist_normalized_image)
    elif red_min and red_max and green_min and green_max and blue_min and blue_max:
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        h, w, c = image.shape
        new_image = np.zeros((h, w, c), np.uint8)
        hist_normalized_image_blue = hist_normalized(image[:, :0], gray_min, gray_max)
        hist_normalized_image_blue = np.round(hist_normalized_image_blue)
        hist_normalized_image_blue = hist_normalized_image_blue.astype(np.uint8)
        hist_normalized_image_green = hist_normalized(image[:, :1], gray_min, gray_max)
        hist_normalized_image_green = np.round(hist_normalized_image_green)
        hist_normalized_image_green = hist_normalized_image_green.astype(np.uint8)
        hist_normalized_image_red = hist_normalized(image[:, :2], gray_min, gray_max)
        hist_normalized_image_red = np.round(hist_normalized_image_red)
        hist_normalized_image_red = hist_normalized_image_red.astype(np.uint8)
        new_image[:, :, 0] = hist_normalized_image_blue
        new_image[:, :, 1] = hist_normalized_image_green
        new_image[:, :, 2] = hist_normalized_image_red
        # 保存图像
        hist_normalized_image_name = f"hist_normalized-rgb-{red_min}-{red_max}-{green_min}-{green_max}-{blue_min}-{blue_max}-{image_name}"
        cv2.imwrite(os.path.join(dir_path, hist_normalized_image_name), new_image)
    else:
        print("gray or rgb normalization range must be set")
        return


if __name__ == "__main__":
    """
    直⽅图正规化
    """
    main()
