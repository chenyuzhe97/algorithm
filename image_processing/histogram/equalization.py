# -*- encoding: utf-8 -*-
"""
@File Name      :   equalization.py
@Create Time    :   2022/9/23 11:26
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


@click.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('--image_type', default='gray', type=str)
def main(image_path, image_type):
    image_name = os.path.basename(image_path)
    dir_path = os.path.dirname(image_path)
    if image_type == 'gray':
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        equalized_image = cv2.equalizeHist(image)
        cv2.imwrite(os.path.join(dir_path, 'equalized_' + image_name), equalized_image)
    elif image_type == 'rgb':
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        b, g, r = cv2.split(image)
        equalized_b = cv2.equalizeHist(b)
        equalized_g = cv2.equalizeHist(g)
        equalized_r = cv2.equalizeHist(r)
        equalized_image = cv2.merge([equalized_b, equalized_g, equalized_r])
        cv2.imwrite(os.path.join(dir_path, 'equalized_' + image_name), equalized_image)
    else:
        raise ValueError('image_type must be gray or rgb')


if __name__ == '__main__':
    """
    直方图均衡化
    """
    main()
