# -*- encoding: utf-8 -*-
"""
@File Name      :   array.py    
@Create Time    :   2021/11/1 18:57
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

array = np.array([2, 4, 1, 3])

# 排序:默认从小到大升序，降序只需要把排序后的数组再使用np.argsort(-A)即可
# 返回排序后的结果:https://numpy.org/devdocs/reference/generated/numpy.sort.html#numpy.sort
# axis:沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序。根据第几维排序，axis=0 按列排序，axis=1 按行排序
# kind是排序算法:quicksort, mergesort, heapsort, stable，默认快排
# order：如果定义了字段，根据字段排序
sorted_array = np.sort(array)
# 返回排序后的索引:https://numpy.org/devdocs/reference/generated/numpy.argsort.html#numpy.argsort
sorted_array_index = np.argsort(array)
# 调用索引排序
array[sorted_array_index]
# 翻转矩阵
reversal_array = array[::-1]

# 二维数组
two_dimensional_array = np.array([
    [4, 2, 5, 6, 1, 3],
    [3, 5, 1, 6, 9, 10]
])
# 行排序
row_sorted_array_index = np.argsort(two_dimensional_array, axis=1)
row_sorted_array = np.take_along_axis(two_dimensional_array, row_sorted_array_index, axis=1)
# 列排序
col_sorted_array_index = np.argsort(two_dimensional_array, axis=0)
col_sorted_array = np.take_along_axis(two_dimensional_array, col_sorted_array_index, axis=0)

# 按指定行或列排序，不修改原数组，返回索引:https://numpy.org/devdocs/reference/generated/numpy.lexsort.html#numpy.lexsort
# 输入一个列表，每一个元素是原数组的某行或某列(从0开始)，写法就是切片
# 使用-1*元素代表降序，优先级是列表从后往前
sorted_array_by_col_1_index = np.lexsort([two_dimensional_array[:, 2]])
sorted_array_by_col_1 = two_dimensional_array[sorted_array_by_col_1_index]
