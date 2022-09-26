# -*- encoding: utf-8 -*-
"""
@File Name      :   max.py
@Create Time    :   2022/9/16 22:33
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

# 自身比较
a = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
])
print(np.max(a, axis=-1))
print(np.max(a, axis=-1, keepdims=True))

# 多个比较
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[2, 4, 1], [3, 7, 4]])
print(np.maximum(a, b))
