# -*- encoding: utf-8 -*-
"""
@File Name      :   distribution.py
@Create Time    :   2022/8/31 11:45
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

import json
import os
from collections import defaultdict

import click
import cv2


def color_count(img):
    h, w = img.shape[:2]
    count = defaultdict(int)
    for i in range(h):
        for j in range(w):
            count[img[i, j]] += 1
    return count


def rgb_hist_distribution(img):
    img_red = img[:, :, 2]
    img_green = img[:, :, 1]
    img_blue = img[:, :, 0]
    red_count = color_count(img_red)
    green_count = color_count(img_green)
    blue_count = color_count(img_blue)
    return {
        'red': dict(sorted(red_count.items(), key=lambda x: x[0])),
        'green': dict(sorted(green_count.items(), key=lambda x: x[0])),
        'blue': dict(sorted(blue_count.items(), key=lambda x: x[0])),
    }


@click.command()
@click.argument('image_path', type=click.Path(exists=True))
def main(image_path: str):
    dir_path = os.path.dirname(image_path)
    img = cv2.imread(image_path)
    print('statistic done')
    with open(os.path.join(dir_path, 'hist_distribution.json'), 'w') as w:
        json.dump(rgb_hist_distribution(img), w)


if __name__ == '__main__':
    """
    图片直方图分布
    """
    main()
