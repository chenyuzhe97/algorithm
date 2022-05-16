# -*- encoding: utf-8 -*-
"""
@File Name      :   python_class_test.py    
@Create Time    :   2022/2/21 11:50
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


class A(object):
    def test(self):
        print(' A test')


class B(A):
    def test(self):
        print(' B test')
        super().test()


class C(A):
    def test(self):
        print(' C test')
        super().test()


class D(A):
    def test(self):
        print(' D test')
        super().test()


class E(B, C):
    def test(self):
        print(' E test')
        super().test()


class F(B, D):
    def test(self):
        print(' F test')
        super().test()


class G(D, C):
    def test(self):
        print(' G test')
        super().test()


class H(E, F, G):
    def test(self):
        print(' H test')
        super().test()


h = H()
h.test()
