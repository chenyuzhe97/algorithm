# -*- encoding: utf-8 -*-
"""
@File Name      :   rgb_mask_gui.py    
@Create Time    :   2022/7/11 10:12
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


def update_mask(bgr_lowers, bgr_uppers, hsv_lowers, hsv_uppers):
    # 计算RGB MASK
    mask_bgr = np.zeros(img.shape[:2], dtype=np.uint8)
    for i in range(3):
        # mask[np.where(np.logical_and(lowers[i]<=img[:,:,i],img[:,:,i]<=uppers[i]))] = 0
        mask_bgr[np.where(np.logical_and(bgr_lowers[i] < img[:, :, i], img[:, :, i] < bgr_uppers[i]))] = 255
    # 计算HSV MASK
    mask_hsv = cv2.inRange(img_hsv, hsv_lowers, hsv_uppers)
    # 合并RGB和HSV MASK
    target = img.copy()
    mask = cv2.bitwise_and(mask_bgr, mask_hsv)
    mask = cv2.bitwise_not(mask)
    for i in range(3):
        target[mask == 255, i] = 0
    # 展示结果
    cv2.imshow('mask', mask)
    cv2.imshow('target', target)


def update_threshold(x):
    bgr_min_b = cv2.getTrackbarPos('bgr_min_b', 'tool_bar')
    bgr_max_b = cv2.getTrackbarPos('bgr_max_b', 'tool_bar')
    bgr_min_g = cv2.getTrackbarPos('bgr_min_g', 'tool_bar')
    bgr_max_g = cv2.getTrackbarPos('bgr_max_g', 'tool_bar')
    bgr_min_r = cv2.getTrackbarPos('bgr_min_r', 'tool_bar')
    bgr_max_r = cv2.getTrackbarPos('bgr_max_r', 'tool_bar')
    bgr_lowers = np.int32([bgr_min_b, bgr_min_g, bgr_min_r])
    bgr_uppers = np.int32([bgr_max_b, bgr_max_g, bgr_max_r])

    hsv_min_h = cv2.getTrackbarPos('hsv_min_h', 'tool_bar')
    hsv_max_h = cv2.getTrackbarPos('hsv_max_h', 'tool_bar')
    hsv_min_s = cv2.getTrackbarPos('hsv_min_s', 'tool_bar')
    hsv_max_s = cv2.getTrackbarPos('hsv_max_s', 'tool_bar')
    hsv_min_v = cv2.getTrackbarPos('hsv_min_v', 'tool_bar')
    hsv_max_v = cv2.getTrackbarPos('hsv_max_v', 'tool_bar')
    hsv_lowers = np.int32([hsv_min_h, hsv_min_s, hsv_min_v])
    hsv_uppers = np.int32([hsv_max_h, hsv_max_s, hsv_max_v])

    update_mask(bgr_lowers, bgr_uppers, hsv_lowers, hsv_uppers)


def adjust(bgr_min_b, bgr_max_b, bgr_min_g, bgr_max_g, bgr_min_r, bgr_max_r, hsv_min_h, hsv_max_h,
           hsv_min_s, hsv_max_s, hsv_min_v, hsv_max_v):
    # 蓝色
    cv2.createTrackbar('bgr_min_b', 'tool_bar', 0, 255, update_threshold)
    cv2.createTrackbar('bgr_max_b', 'tool_bar', 0, 255, update_threshold)
    # 绿色
    cv2.createTrackbar('bgr_min_g', 'tool_bar', 0, 255, update_threshold)
    cv2.createTrackbar('bgr_max_g', 'tool_bar', 0, 255, update_threshold)
    # 红色
    cv2.createTrackbar('bgr_min_r', 'tool_bar', 0, 255, update_threshold)
    cv2.createTrackbar('bgr_max_r', 'tool_bar', 0, 255, update_threshold)
    # 色度
    cv2.createTrackbar('hsv_min_h', 'tool_bar', 0, 179, update_threshold)
    cv2.createTrackbar('hsv_max_h', 'tool_bar', 0, 179, update_threshold)
    # 饱和度
    cv2.createTrackbar('hsv_min_s', 'tool_bar', 0, 255, update_threshold)
    cv2.createTrackbar('hsv_max_s', 'tool_bar', 0, 255, update_threshold)
    # 明度
    cv2.createTrackbar('hsv_min_v', 'tool_bar', 0, 255, update_threshold)
    cv2.createTrackbar('hsv_max_v', 'tool_bar', 0, 255, update_threshold)

    # 初始化
    # rgb
    cv2.setTrackbarPos('bgr_min_b', 'tool_bar', bgr_min_b)
    cv2.setTrackbarPos('bgr_max_b', 'tool_bar', bgr_max_b)
    cv2.setTrackbarPos('bgr_min_g', 'tool_bar', bgr_min_g)
    cv2.setTrackbarPos('bgr_max_g', 'tool_bar', bgr_max_g)
    cv2.setTrackbarPos('bgr_min_r', 'tool_bar', bgr_min_r)
    cv2.setTrackbarPos('bgr_max_r', 'tool_bar', bgr_max_r)
    # hsv
    cv2.setTrackbarPos('hsv_min_h', 'tool_bar', hsv_min_h)
    cv2.setTrackbarPos('hsv_max_h', 'tool_bar', hsv_max_h)
    cv2.setTrackbarPos('hsv_min_s', 'tool_bar', hsv_min_s)
    cv2.setTrackbarPos('hsv_max_s', 'tool_bar', hsv_max_s)
    cv2.setTrackbarPos('hsv_min_v', 'tool_bar', hsv_min_v)
    cv2.setTrackbarPos('hsv_max_v', 'tool_bar', hsv_max_v)
    # 初始化窗口，后面的更新由 updateBGRThreshold 产生变化而触发
    update_threshold(None)


@click.command()
@click.argument('image_path', type=click.Path(exists=True))
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
def main(image_path, bgr_min_b, bgr_max_b, bgr_min_g, bgr_max_g, bgr_min_r, bgr_max_r, hsv_min_h, hsv_max_h,
         hsv_min_s, hsv_max_s, hsv_min_v, hsv_max_v):
    global img
    img = cv2.imread(image_path)
    img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)

    global img_bgr
    img_bgr = img.copy()

    global img_hsv
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.namedWindow('tool_bar', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
    adjust(bgr_min_b, bgr_max_b, bgr_min_g, bgr_max_g, bgr_min_r, bgr_max_r, hsv_min_h, hsv_max_h,
           hsv_min_s, hsv_max_s, hsv_min_v, hsv_max_v)
    print("调整阈值, 按q键退出程序")
    while cv2.waitKey(0) != ord('q'):
        continue
    cv2.destroyAllWindows()


if __name__ == '__main__':
    """
    示例：python ./image_processing/mask/rgb_mask_gui.py 图片绝对路径
    """
    main()
