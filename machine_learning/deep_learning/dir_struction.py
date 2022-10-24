# -*- encoding: utf-8 -*-
"""
@File Name      :   dir_struction.py
@Create Time    :   2021/10/1 19:14
@Description    :   
@Version        :   
@License        :   
@Author         :   diklios
@Contact Email  :   diklios5768@gmail.com
@Github         :   https://github.com/diklios5768
@Blog           :   
@Motto          :   All our science, measured against reality, is primitive and childlike - and yet it is the most precious thing we have.
"""
__auth__ = 'diklios'

import os

dir_paths = [
    # 创建 outputs 文件夹，用于存放生成结果
    'outputs',
    # 创建 data 文件夹，用于存放图像数据集
    'data',
    # 创建 checkpoints 文件夹，用于存放模型权重文件
    'checkpoints',
    # 创建 work_dirs 文件夹，用于存放训练结果及趣味 demo 输出结果
    'work_dirs'
    'logs',
    # 创建 results 文件夹，用于存放训练过程中模型各项参数的变化和临时结果
    'results'
]

for dir_path in dir_paths:
    if not (os.path.exists(dir_path) and os.path.isdir(dir_path)):
        os.mkdir(dir_path)
        print(f'{dir_path}文件夹创建成功')
