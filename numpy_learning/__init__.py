# -*- encoding: utf-8 -*-
"""
@File Name      :   __init__.py    
@Create Time    :   2021/9/25 8:45
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
# 数组转矩阵
# np.array()
# 矩阵的逆
# np.linalg.inv()

# A = np.array([[[0,1,2], [3 ,4, 5]],[[6,7,8],[9,10,11]]])
# B = np.array([[[0 ,1],[2,3],[4,5]],[[6,7],[8,9],[10,11]]])
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([1, 2, 3])

# 点乘，即对位相乘，需要m,n都相同
# print(A * B)
# print(np.multiply(A, B))
# 叉乘，零维的时候是标量相乘，当是一维向量的时候就是向量内积，二维的时候是矩阵乘积。还支持标量与矩阵相乘，此时等同于multiply，更复杂的情况见文档
print(np.dot(A, B))
# 正常矩阵乘法，在一维和二维的时候和dot是一样的。不支持标量相乘，即零维相乘。不支持标量与矩阵相乘
# print(np.matmul(A, B.T))
# print(A @ B)
