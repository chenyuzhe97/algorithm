# -*- encoding: utf-8 -*-
"""
@File Name      :   mask_extract.py    
@Create Time    :   2022/8/27 16:18
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




def extract(image_path: str, threshold: int):
    dir_name = os.path.dirname(image_path)
    raw_file_name = os.path.basename(image_path)
    mask_file_path = os.path.join(dir_name, f'mask-{raw_file_name}')
    img = cv2.imread(image_path)
    img2 = img.copy()
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2[img_grey >= threshold] = 255
    cv2.imwrite(mask_file_path, img2)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--threshold_default', '-t', default=10, help='threshold')
def main(path: str, threshold_default: int):
    # 处理单文件
    if os.path.isfile(path):
        extract(path, threshold_default)
    # 处理文件夹
    elif os.path.isdir(path):
        for file_path in os.listdir(path):
            extract(os.path.join(path, file_path), threshold_default)
    else:
        print('wrong use')
        return


if __name__ == '__main__':
    """
    从被mask遮住的图中只提取mask
    """
    main()
