# -*- encoding: utf-8 -*-
"""
@File Name      :   mask.py    
@Create Time    :   2022/7/8 16:00
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
import time

import click
import cv2
import numpy as np


def handle_image(image_path, bgr_min_b, bgr_max_b, bgr_min_g, bgr_max_g, bgr_min_r, bgr_max_r, hsv_min_h, hsv_max_h,
                 hsv_min_s, hsv_max_s, hsv_min_v, hsv_max_v):
    print(f'{image_path} start')
    start_time = time.perf_counter()
    img = cv2.imread(image_path)
    img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
    img_bgr = img.copy()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bgr_lowers = np.int32([bgr_min_b, bgr_min_g, bgr_min_r])
    bgr_uppers = np.int32([bgr_max_b, bgr_max_g, bgr_max_r])
    hsv_lowers = np.int32([hsv_min_h, hsv_min_s, hsv_min_v])
    hsv_uppers = np.int32([hsv_max_h, hsv_max_s, hsv_max_v])
    # 计算RGB MASK
    mask_bgr = np.zeros(img_bgr.shape[:2], dtype=np.uint8)
    for i in range(3):
        # mask[np.where(np.logical_and(lowers[i]<=img[:,:,i],img[:,:,i]<=uppers[i]))] = 0
        mask_bgr[np.where(np.logical_and(bgr_lowers[i] <= img_bgr[:, :, i], img_bgr[:, :, i] <= bgr_uppers[i]))] = 255
    # 计算HSV MASK
    mask_hsv = cv2.inRange(img_hsv, hsv_lowers, hsv_uppers)
    # 合并RGB和HSV MASK
    target = img.copy()
    mask = cv2.bitwise_and(mask_bgr, mask_hsv)
    mask = cv2.bitwise_not(mask)
    for i in range(3):
        target[mask == 0, i] = 0
    # 保存结果
    dir_path = os.path.dirname(image_path)
    image_name = os.path.basename(image_path)
    cv2.imwrite(os.path.join(dir_path, 'mask_' + image_name), mask)
    cv2.imwrite(os.path.join(dir_path, 'target_' + image_name), target)
    print(f'{image_path} finished, time: {time.perf_counter() - start_time}')


@click.command()
@click.option('--image_path', '-i', default='', help='image path')
@click.option('--dir_path', '-d', default='', help='image dir path')
@click.option('--bgr_min_b', '-bgr_b', default=0, help='bgr_min_b')
@click.option('--bgr_max_b', '-bgr_B', default=255, help='bgr_max_b')
@click.option('--bgr_min_g', '-bgr_g', default=0, help='bgr_min_g')
@click.option('--bgr_max_g', '-bgr_G', default=255, help='bgr_max_g')
@click.option('--bgr_min_r', '-bgr_r', default=0, help='bgr_min_r')
@click.option('--bgr_max_r', '-bgr_R', default=255, help='bgr_max_r')
@click.option('--hsv_min_h', '-hsv_h', default=0, help='hsv_min_h')
@click.option('--hsv_max_h', '-hsv_H', default=179, help='hsv_max_h')
@click.option('--hsv_min_s', '-hsv_s', default=0, help='hsv_min_s')
@click.option('--hsv_max_s', '-hsv_S', default=255, help='hsv_max_s')
@click.option('--hsv_min_v', '-hsv_v', default=0, help='hsv_min_v')
@click.option('--hsv_max_v', '-hsv_V', default=255, help='hsv_max_v')
def main(image_path, dir_path, bgr_min_b, bgr_max_b, bgr_min_g, bgr_max_g, bgr_min_r, bgr_max_r, hsv_min_h, hsv_max_h,
         hsv_min_s, hsv_max_s, hsv_min_v, hsv_max_v):
    if not image_path and not dir_path:
        print('image_path or dir_path must be set')
        return
    if image_path:
        handle_image(image_path, bgr_min_b, bgr_max_b, bgr_min_g, bgr_max_g, bgr_min_r, bgr_max_r, hsv_min_h, hsv_max_h,
                     hsv_min_s, hsv_max_s, hsv_min_v, hsv_max_v)
    if dir_path:
        images_names = os.listdir(dir_path)
        for image_name in images_names:
            image_path = os.path.join(dir_path, image_name)
            handle_image(image_path, bgr_min_b, bgr_max_b, bgr_min_g, bgr_max_g, bgr_min_r, bgr_max_r, hsv_min_h,
                         hsv_max_h, hsv_min_s, hsv_max_s, hsv_min_v, hsv_max_v)


if __name__ == '__main__':
    """
    示例：python ./image_processing/mask/rgb_mask.py --dir_path 文件夹绝对路径 --hsv_min_h=3 --hsv_max_h=30 --hsv_min_s=60 --hsv_max_s=150 --hsv_min_v=40 --hsv_max_v=255
    """
    main()
