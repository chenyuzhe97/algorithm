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
# 矩阵的逆
np.linalg.inv()