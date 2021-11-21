# -*- encoding: utf-8 -*-
"""
@File Name      :   mnist.py
@Create Time    :   2021/11/15 14:46
@Description    :   MNIST手写数字识别的原生python3神经网络代码（原来的是python2），数据和代码：git clone https://github.com/mnielsen/neural-networks-and-deep-learning.git
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

import random

import numpy as np
from .mnist_load_data import *


def sigmoid(z: float or np.array):
    """
    S型神经元的激活函数
    :param z:可以是一个数，也可以是一个numpy的向量
    :return:一个数或者numpy向量
    """
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    """
    Derivative of the sigmoid function.
    """
    return sigmoid(z) * (1 - sigmoid(z))


class Network(object):
    """
    :param sizes:各层神经元数量的列表
    偏重和权重都是被随机初始化的
    :param self.biases:偏置
    :param self.weights:权重

    """

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        # n层神经网络只需要除第一个神经元（输入层无偏置）的n-1个偏置
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        # n层神经元需要除最后一个神经元的(n-1)层*(m)个权重，m在每一层都不同
        # 这里的y放前面是为了和前面的偏置保持相同的维度
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        """
        ⽹络给定⼀个输⼊ a，返回对应的输出，这个⽅法所做的是对每⼀层应⽤sigmoid⽅程
        Return the output of the network if "a" is input.
        """
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a

    def backpropagation(self, x, y):
        """
        反向传播

        Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x. ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``.
        """

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]  # list to store all the activations, layer by layer
        zs = []  # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book. Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on. It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l + 1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l - 1].transpose())
        return nabla_b, nabla_w

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""

        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """
        Return the vector of partial derivatives partial C_x / partial a for the output activations.
        """
        return output_activations - y

    def update_mini_batch(self, mini_batch, eta):
        """
        对于每⼀个 mini_batch应⽤⼀次梯度下降，它仅仅使⽤ mini_batch 中的训练数据，根据单次梯度下降的迭代更新⽹络的权重和偏置
        :param mini_batch:⼩批量数据
        :param eta:步长

        Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The "mini_batch" is a list of tuples "(x, y)", and "eta"
        is the learning rate.
        """

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            # 反向传播
            delta_nabla_b, delta_nabla_w = self.backpropagation(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
            # 更新权重和偏置
            self.weights = [w - (eta / len(mini_batch)) * nw for w, nw in zip(self.weights, nabla_w)]
            self.biases = [b - (eta / len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b)]

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        """
        随机梯度下降
        :param training_data:是⼀个 (x, y) 元组的列表，表⽰训练输⼊和其对应的期望输出
        :param epochs:迭代期数量
        :param mini_batch_size:采样时的⼩批量数据的⼤⼩
        :param eta:学习速率（步长）η
        :param test_data:测试数据，如果给出，那么程序会在每个训练器后评估⽹络，并打印出部分进展。这对于追踪进度很有⽤，但相当拖慢执⾏速度。
        Train the neural network using mini-batch stochastic
        gradient descent. The "training_data" is a list of tuples
        "(x, y)" representing the training inputs and the desired
        outputs. The other non-optional parameters are
        self-explanatory. If "test_data" is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out. This is useful for
        tracking progress, but slows things down substantially.
        """
        n = len(training_data)
        if test_data:
            n_test = len(test_data)
        else:
            n_test = 0
        # 在每个迭代期，它⾸先随机地将训练数据打乱，然后将它分成多个适当⼤⼩的⼩批量数据。这是⼀个简单的从训练数据的随机采样⽅法
        for j in range(epochs):
            # 打乱
            random.shuffle(training_data)
            # 分成多个适当⼤⼩的⼩批量数据
            mini_batches = [training_data[k:k + mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                # 每用一个数据集更新一次权重和偏置
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test))
            else:
                print("Epoch {0} complete".format(j))


if __name__ == '__main__':
    training_data, validation_data, test_data = load_data_wrapper()
    net = Network([784, 30, 10])
    net.SGD(training_data, 30, 10, 3.0, test_data=test_data)