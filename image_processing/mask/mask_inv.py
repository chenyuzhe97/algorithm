# -*- encoding: utf-8 -*-
"""
@File Name      :   mask_inv.py    
@Create Time    :   2022/8/27 16:16
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
@click.argument('raw_image_path', type=click.Path(exists=True))
@click.argument('mask_image_path', type=click.Path(exists=True))
@click.option('--threshold_default', '-t', default=10, help='threshold')
def main(raw_image_path: str, mask_image_path: str, threshold_default: int):
    img_raw = cv2.imread(raw_image_path)
    img_mask = cv2.imread(mask_image_path)
    dir_name = os.path.dirname(raw_image_path)
    mask_file_name = os.path.basename(mask_image_path)
    inv_mask_file_path = os.path.join(dir_name, f'inv-{mask_file_name}')
    img_mask = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)
    img_mask = cv2.resize(img_mask, (img_raw.shape[1], img_raw.shape[0]), cv2.INTER_CUBIC)
    img_raw[img_mask >= threshold_default, :] = 0
    cv2.imwrite(inv_mask_file_path, img_raw)


if __name__ == '__main__':
    """
    将mask取反，需要原图
    """
    main()
