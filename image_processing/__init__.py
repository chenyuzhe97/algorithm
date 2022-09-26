# -*- encoding: utf-8 -*-
"""
@File Name      :   __init__.py
@Create Time    :   2022/9/4 13:55
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

import numpy as np


def color_unification(img: np.Arrayterator, range_down: int = 0, range_up: int = 20,
                      rang_to: int = 0) -> np.Arrayterator:
    """
    将图片中的颜色统一化
    :param img: 图片
    :param rang_to: 统一后的颜色
    :param range_up: 颜色范围上限
    :param range_down: 颜色范围下限
    :return: 统一化后的图片
    """
    channel = img.shape[2]
    if channel == 1:
        img[range_down <= img <= range_up] = rang_to
    elif channel == 3:
        img[np.logical_and.reduce((
            range_down <= img[:, :, 0] <= range_up,
            range_down <= img[:, :, 1] <= range_up,
            range_down <= img[:, :, 2] <= range_up
        ))] = rang_to
    return img
