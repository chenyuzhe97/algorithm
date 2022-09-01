# -*- encoding: utf-8 -*-
"""
@File Name      :   mean_statistic.py    
@Create Time    :   2022/8/31 11:41
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


def is_json_file(file_path: str):
    return os.path.isfile(file_path) and '~$' not in file_path and file_path.endswith('.json')


def color_count(img):
    h, w = img.shape[:2]
    count = defaultdict(int)
    for i in range(h):
        for j in range(w):
            count[img[i, j]] += 1

    return count


def merge_dict(x: defaultdict, y: dict):
    for k, v in y.items():
        x[k] += v


def count_mean(count: dict, num: int):
    return {int(k): v / num for k, v in count.items()}


@click.command()
@click.argument('dir_path', type=click.Path(exists=True))
def main(dir_path: str):
    file_paths = [os.path.join(dir_path, file_name) for file_name in os.listdir(dir_path)]
    image_paths = [file_path for file_path in file_paths if os.path.isfile(file_path) and not is_json_file(file_path)]
    num = len(image_paths)
    red_count = defaultdict(int)
    green_count = defaultdict(int)
    blue_count = defaultdict(int)
    for image_path in image_paths:
        img = cv2.imread(image_path)
        img_red = img[:, :, 2]
        img_green = img[:, :, 1]
        img_blue = img[:, :, 0]
        merge_dict(red_count, color_count(img_red))
        merge_dict(green_count, color_count(img_green))
        merge_dict(blue_count, color_count(img_blue))
        print(f'process {image_path} done')
    print('statistic done')
    with open(os.path.join(dir_path, 'mean_his_distribution.json'), 'w') as w:
        json.dump({
            'red': dict(sorted(count_mean(red_count, num).items(), key=lambda x: x[0])),
            'green': dict(sorted(count_mean(green_count, num).items(), key=lambda x: x[0])),
            'blue': dict(sorted(count_mean(blue_count, num).items(), key=lambda x: x[0])),
        }, w)


if __name__ == '__main__':
    """
    数据集直方图分布统计
    """
    main()
