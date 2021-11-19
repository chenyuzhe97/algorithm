# -*- encoding: utf-8 -*-
"""
@File Name      :   reduced_echelon_matrix.py    
@Create Time    :   2021/9/25 9:18
@Description    :   echelon matrix(阶梯形矩阵)
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
from sympy import Matrix


# 化为行最简
# 使用numpy
def rsmat(arbmat):
    """ Convert an arbitrary matrix to a simplest matrix """
    arbmat = arbmat.astype(float)
    row_number, column_number = arbmat.shape
    if row_number == 1:
        if arbmat[0, 0] != 0:
            return (arbmat / arbmat[0, 0])
        else:
            return arbmat
    else:
        rc_number = min(row_number, column_number)
        anarbmat = arbmat.copy()
        r = 0
        for n in range(rc_number):
            s_row = -1
            for i in arbmat[r:row_number, n]:
                s_row += 1
                if abs(i) > 1e-10:
                    anarbmat[r, :] = arbmat[s_row + r, :]
                    for j in range(r, row_number):
                        if j < s_row + r:
                            anarbmat[j + 1, :] = arbmat[j, :]
                    arbmat = anarbmat.copy()
            if abs(anarbmat[r, n]) > 1e-10:
                anarbmat[r, :] = anarbmat[r, :] / anarbmat[r, n]
                for i in range(row_number):
                    if i != r:
                        anarbmat[i, :] -= \
                            anarbmat[i, n] * anarbmat[r, :]
            arbmat = anarbmat.copy()
            if abs(arbmat[r, n]) < 1e-10:
                r = r
            else:
                r = r + 1
        for m in range(column_number):
            if abs(arbmat[-1, m]) > 1e-10:
                arbmat[-1, :] = arbmat[-1, :] / arbmat[-1, m]
                for i in range(row_number - 1):
                    arbmat[i, :] -= \
                        arbmat[i, m] * arbmat[-1, :]
                break
        return arbmat


# 使用sympy
rref = Matrix(np.array([
    [1, 0, 3, 2],
    [1, 2, 1, -4],
    [1, 1, 0, -3],
    [2, 3, 1, -7]
])).rref()[0].tolist()
print(rref)
