# -*- encoding: utf-8 -*-
"""
@File Name      :   random.py    
@Create Time    :   2021/11/15 15:00
@Description    :   
@Version        :   
@License        :   
@Author         :   diklios
@Contact Email  :   diklios5768@gmail.com
@Github         :   https://github.com/diklios5768
@Blog           :   
@Motto          :   All our science, measured against reality, is primitive and childlike - and yet it is the most precious thing we have.
@other information
"""
__auth__ = 'diklios'

import numpy as np

# 从[0-1)产生随机样本值，输入需要的维度
np.random.rand(2, 4)

# 从标准正态分布中返回随机样本值，输入需要的维度
# 是以0为均值、以1为标准差的正态分布，记为N(0，1)
np.random.randn(2, 4)

# 产生随机整数，范围为[low,high),size为维度，dtype为数据类型，默认的数据类型是np.int
# high没有填写时，默认生成随机数的范围是[0，low)
np.random.randint(1, 10, [2, 4])

# 生成[0,1)之间的浮点数
np.random.random_sample()
# ranf是random_sample的别名
np.random.ranf()
# sample同样是random_sample的别名
np.random.sample()
# random也是random_sample的别名
np.random.random()

# 从给定的一维数组中生成随机数
# 参数： a为一维数组类似数据或整数；size为数组维度；
# p为数组中的数据出现的概率,参数p的长度与参数a的长度需要一致,参数p为概率，p里的数据之和应为1
# 当replace为False时，生成的随机数不能有重复的数值
np.random.choice(5, 3)

# 使得随机数据可预测
# 当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
np.random.seed(10)
