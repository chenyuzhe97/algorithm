# -*- encoding: utf-8 -*-
"""
@File Name      :   specification_med_img.py
@Create Time    :   2022/9/26 14:38
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

from specification import calc_probability_distribution

black_threshold = 5


def calc_hist(image):
    mat = np.array(image)
    return [len(mat[mat == i]) for i in range(black_threshold, 256)]


def get_infer_map(image):
    hist = calc_hist(image)
    infer_map = calc_probability_distribution(hist)
    return infer_map


def get_final_map(reflect_image_map, source_image_map):
    # 原图像素点映射到目标图的map
    final_map = [0 for i in range(black_threshold)]
    index = 0
    upper_limit = 255 - black_threshold
    for i in range(len(source_image_map)):
        # 防⽌像素值超过255
        if index == upper_limit:
            final_map.append(upper_limit)
            continue
        # 将像素值依据自身概率分布映射到目标图⽚的概率分布上
        if reflect_image_map[index] > source_image_map[i]:
            final_map.append(index)
        else:
            while reflect_image_map[index] <= source_image_map[i]:
                index += 1
                # 防⽌像素值超过255
                if index == upper_limit:
                    break
            final_map.append(index)
    return final_map


def get_new_img(source_image, reflect_image):
    specified_img = source_image.copy()
    # 计算参考映射关系
    source_image_map = get_infer_map(source_image)
    reflect_image_map = get_infer_map(reflect_image)
    final_map = get_final_map(reflect_image_map, source_image_map)
    for i in range(black_threshold, 256):
        specified_img[source_image == i] = final_map[i]
    specified_img[source_image <= black_threshold] = 0

    return specified_img


@click.command()
@click.argument('source_image_path', type=click.Path(exists=True))
@click.argument('reflect_image_path', type=click.Path(exists=True))
@click.option('--image_type', default='gray', type=str)
def main(source_image_path, reflect_image_path, image_type):
    # 以原图文件夹为存储地点
    source_image_dir_path = os.path.dirname(source_image_path)
    source_image_name = os.path.basename(source_image_path)
    if image_type == 'gray':
        source_image = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)
        reflect_image = cv2.imread(reflect_image_path, cv2.IMREAD_GRAYSCALE)
        # 根据映射关系获得新的图像
        specified_image = get_new_img(source_image, reflect_image)
        # 保存新图像
        cv2.imwrite(os.path.join(source_image_dir_path, 'specified_' + source_image_name), specified_image)
    elif image_type == 'rgb':
        source_image = cv2.imread(source_image_path, cv2.IMREAD_COLOR)
        source_image_b, source_image_g, source_image_r = cv2.split(source_image)
        reflect_image = cv2.imread(reflect_image_path, cv2.IMREAD_COLOR)
        reflect_image_b, reflect_image_g, reflect_image_r = cv2.split(reflect_image)
        specified_image_b = get_new_img(source_image_b, reflect_image_b)
        specified_image_g = get_new_img(source_image_g, reflect_image_g)
        specified_image_r = get_new_img(source_image_r, reflect_image_r)
        specified_image = cv2.merge([specified_image_b, specified_image_g, specified_image_r])
        cv2.imwrite(os.path.join(source_image_dir_path, 'specified_' + source_image_name), specified_image)
    else:
        raise ValueError('image_type must be gray or rgb')


if __name__ == '__main__':
    """
    医学图像专用的直方图规定化
    """
    main()
