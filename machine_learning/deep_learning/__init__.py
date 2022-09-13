# -*- encoding: utf-8 -*-
"""
@File Name      :   __init__.py    
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

# 创建 outputs 文件夹，用于存放生成结果
os.mkdir('outputs')

# 创建 data 文件夹，用于存放图像数据集
os.mkdir('data')

# 创建 checkpoints 文件夹，用于存放模型权重文件
os.mkdir('checkpoints')

# 创建 work_dirs 文件夹，用于存放训练结果及趣味 demo 输出结果
os.mkdir('work_dirs')
