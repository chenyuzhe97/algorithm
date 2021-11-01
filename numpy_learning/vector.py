# -*- encoding: utf-8 -*-
"""
@File Name      :   vector.py    
@Create Time    :   2021/10/19 9:57
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

import numpy as np
import fractions

# 设置显示为分数
np.set_printoptions(formatter={'all': lambda x: str(fractions.Fraction(x).limit_denominator())})

# 定义矩阵
A = np.mat([
    [1, 0, 3, 2],
    [1, 2, 1, -4],
    [1, 1, 0, -3],
    [2, 3, 1, -7]
])
# 矩阵的转置
A.T
# 矩阵的逆
A.I
# 矩阵的行列式，得到矩阵是否是非奇异的
det = np.linalg.det(A)
# 矩阵的秩
rank = np.linalg.matrix_rank(A)
# 求特征值和特征向量
value, vector = np.linalg.eig(A)
