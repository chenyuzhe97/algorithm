# -*- encoding: utf-8 -*-
"""
@File Name      :   solution.py    
@Create Time    :   2021/9/25 9:30
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

from sympy import *
from sympy.abc import a, b, c, d

# 使用latex显示
init_printing(use_latex=True)
# 定义变量
x1, x2, x3, x4 = S('x1,x2,x3,x4')


# 求方程组的解
# 定义增广矩阵
matrix = Matrix([[1, -1, -2, -1, 0], [2, 1, 1, 1, 0], [1, 1, 0, -3, 0], [0, 1, -1, -7, 0]])
# 求解
res = solve_linear_system(matrix, a, b, c, d)
