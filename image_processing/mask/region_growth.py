# -*- encoding: utf-8 -*-
"""
@File Name      :   region_growth3.py    
@Create Time    :   2022/7/20 14:23
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
import random
from copy import deepcopy

import click
import cv2
import numpy as np

global img, img_red, img_seeds, img_pixels, mask, target, h, w
mask_color = 255
threshold = 1
seeds = []


class Pixel:
    def __init__(self, x, y, value, status=False):
        self.x = x
        self.y = y
        self.value = value
        self.status = status


def safe_index(x, y):
    global w, h

    if w > x >= 0 and h > y >= 0:
        return True
    else:
        return False


def check_neighbors(pixels, current_pixel, lower_bound, upper_bound):
    neighbors = []
    x = current_pixel.x
    y = current_pixel.y

    # 8邻域
    if safe_index(x, y + 1):
        top = pixels[y + 1][x]
    else:
        top = Pixel(0, 0, 0, True)
    if safe_index(x, y - 1):
        down = pixels[y - 1][x]
    else:
        down = Pixel(0, 0, 0, True)
    if safe_index(x - 1, y):
        left = pixels[y][x - 1]
    else:
        left = Pixel(0, 0, 0, True)
    if safe_index(x + 1, y):
        right = pixels[y][x + 1]
    else:
        right = Pixel(0, 0, 0, True)
    if safe_index(x - 1, y + 1):
        top_left = pixels[y + 1][x - 1]
    else:
        top_left = Pixel(0, 0, 0, True)
    if safe_index(x + 1, y + 1):
        top_right = pixels[y + 1][x + 1]
    else:
        top_right = Pixel(0, 0, 0, True)
    if safe_index(x - 1, y - 1):
        down_left = pixels[y - 1][x - 1]
    else:
        down_left = Pixel(0, 0, 0, True)
    if safe_index(x + 1, y - 1):
        down_right = pixels[y - 1][x + 1]
    else:
        down_right = Pixel(0, 0, 0, True)

    if not top.status and lower_bound < top.value < upper_bound:
        neighbors.append(top)
    if not down.status and lower_bound < down.value < upper_bound:
        neighbors.append(down)
    if not left.status and lower_bound < left.value < upper_bound:
        neighbors.append(left)
    if not right.status and lower_bound < right.value < upper_bound:
        neighbors.append(right)
    if not top_left.status and lower_bound < top_left.value < upper_bound:
        neighbors.append(top_left)
    if not top_right.status and lower_bound < top_right.value < upper_bound:
        neighbors.append(top_right)
    if not down_left.status and lower_bound < down_left.value < upper_bound:
        neighbors.append(down_left)
    if not down_right.status and lower_bound < down_right.value < upper_bound:
        neighbors.append(down_right)

    # pick random neighbor to check
    if len(neighbors) > 0:
        r = random.randint(0, len(neighbors) - 1)
        return neighbors[r]
    else:
        return None


def region_growth(seed: tuple):
    seed_x, seed_y = seed
    current_color = img_red[seed_y, seed_x]
    seed_mask = np.zeros(img_red.shape[:2], dtype=np.uint8)
    pixels = deepcopy(img_pixels)
    current_pixel = pixels[seed_y][seed_x]
    still_searching = True

    # allows us to backtrack visited pixels
    stack = []
    while still_searching:
        current_pixel.status = True
        next_pixel = check_neighbors(pixels, current_pixel, current_color - threshold, current_color + threshold)
        if next_pixel is not None:
            seed_mask[next_pixel.y, next_pixel.x] = mask_color
            stack.append(current_pixel)
            current_pixel = next_pixel
        elif len(stack) > 0:
            current_pixel = stack[-1]
            stack.pop(-1)
        else:
            still_searching = False
    print(np.sum(seed_mask == 255))

    return seed_mask


def update_mask(v):
    global img, threshold, mask, target
    threshold = v
    seed_masks = [region_growth(seed) for seed in seeds]
    mask = np.zeros(img_red.shape[:2], dtype=np.uint8)
    for seed_mask in seed_masks:
        mask[seed_mask == 255] = 255

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    target = img.copy()
    target[mask == 0, :] = 0
    cv2.imshow('mask', mask)
    cv2.imshow('target', target)


def mouse_event(event, x, y, flags, param):
    # 左击鼠标
    if event == cv2.EVENT_LBUTTONDOWN:
        # 添加种子
        seeds.append((x, y))
        # 画实心点
        cv2.circle(img_seeds, center=(x, y), radius=2, color=(0, 0, 255), thickness=-1)
        cv2.imshow('img', img_seeds)
        update_mask(threshold)


@click.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('--threshold_default', '-t', default=15, help='threshold')
def main(image_path, threshold_default):
    global img
    img = cv2.imread(image_path)
    # 重新创建一个数组赋值，防止引用改变原始图像
    global img_red, img_seeds, img_pixels, mask, target, h, w
    img_red = np.zeros(img.shape[:2], dtype=np.uint8)
    # cv2是bgr
    img_red[:, :] = img[:, :, 2]
    # img_red[:, :] = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_seeds = img.copy()
    h, w = img_red.shape[:2]
    img_pixels = [[Pixel(x, y, img_red[y, x]) for x in range(w)] for y in range(h)]
    # 创建一个窗口
    cv2.namedWindow('img')
    cv2.imshow('img', img_seeds)
    # 创建阈值滑动条
    global threshold
    threshold = threshold_default
    cv2.createTrackbar('threshold', 'img', 0, 20, update_mask)
    cv2.setTrackbarPos('threshold', 'img', threshold)
    # 监听鼠标事件，添加种子
    global seeds
    cv2.setMouseCallback('img', mouse_event)

    stop = False
    while not stop:
        key = cv2.waitKey(0)
        if key == ord('q'):
            stop = True
        elif key == ord('s'):
            dir_path = os.path.dirname(image_path)
            image_name = os.path.basename(image_path)
            print(f'{image_name}保存图片到{dir_path}')
            cv2.imwrite(os.path.join(dir_path, 'mask_' + image_name), mask)
            cv2.imwrite(os.path.join(dir_path, 'target_' + image_name), target)
        elif key == ord('c'):
            seeds = []
            img_seeds = img.copy()
            cv2.imshow('img', img_seeds)
            update_mask(threshold)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    """
    区域生长算法
    """
    main()
