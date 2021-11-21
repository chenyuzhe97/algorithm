# 用于学习和测试算法的项目

<p align="center">
<a href="https://github.com/diklios5768" target="_blank">
<img alt="Github" src="https://img.shields.io/badge/作者-@diklios-000000.svg?style=flat-square&logo=GitHub">
</a>
<a href="https://github.com/diklios5768/algorithm" target="_blank">
<img alt="GitHub" src="https://img.shields.io/github/stars/diklios5768/algorithm?label=Stars&style=flat-square&logo=GitHub">
</a>
</p>

## 安装环境

* 安装python（推荐3.6以上的版本，且附带pip）
* 在终端中输入：`pip install pipenv`
    * 尽量能够使用代理
    * 如果不方便使用代理，请百度`pip`换源教程
    * 最后在`Pipfile`文件中注释`pypi`源，换为任意一个国内的源

* 设置环境变量
    * 创建.env文件
    * 文件内容参考如下：

```dotenv
#可以使用PIPENV_VENV_IN_PROJECT环境变量让环境创建在当前项目目录下
PIPENV_VENV_IN_PROJECT=1
#保持其他包不更新，因为pipenv install/update 会默认更新所有包
PIPENV_KEEP_OUTDATED=1
#默认不清除缓存
PIPENV_CLEAR=0
```

* 进入到当前项目文件夹，运行命令：`pipenv install`
    * 如果保错请安装`c++ build tools 14`以上的版本（一般在报错的终端提示中会有链接）
        * 或者直接安装visual studio 2017以上的版本，选择c++工具包
    * 如果网络连接不上，建议更改终端代理或者对pip进行换源
    * 如果提示没有python某版本，在Pipfile文件最后更改，默认是3.9

## 参考资料

* 机器学习和深度学习
    * github项目
        * [ML-notes](https://github.com/Sakura-gh/ML-notes)
        * [AI learning](https://github.com/apachecn/AiLearning)
        * [斯坦福大学2014（吴恩达）机器学习教程中文笔记](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes)
        * [动手学深度学习](https://github.com/d2l-ai/d2l-zh)
            * [《动手学深度学习》PyTorch代码实现](https://github.com/ShusenTang/Dive-into-DL-PyTorch)
                * https://tangshusen.me/Dive-into-DL-PyTorch
            * [《动手学深度学习》TensorFlow2.0代码实现](https://github.com/TrickyGo/Dive-into-DL-TensorFlow2.0)
                * https://trickygo.github.io/Dive-into-DL-TensorFlow2.0
            * 李沐的《动手学深度学习》在线版
                * http://zh.d2l.ai/
                * https://zh-v2.d2l.ai/
    * 课程
        * [吴恩达机器学习系列课程](https://www.bilibili.com/video/BV164411b7dx)
        * [李宏毅2020版机器学习深度学习](https://www.bilibili.com/video/BV1JE411g7XF)
        * [李宏毅《机器学习/深度学习》2021版课程](https://www.bilibili.com/video/BV1JA411c7VT)
        * [吴恩达深度学习](https://www.bilibili.com/video/BV1FT4y1E74V)
    * 书籍
        * 周志华的《机器学习》
        * 神经网络与深度学习，邱锡鹏，在线版：https://nndl.github.io/
        * 《深度学习》（花书）
        * [机器学习基础在线版](https://mitpress.ublish.com/ereader/7093/?preview=#page/1)
            * 下载PDF：https://cs.nyu.edu/~mohri/mlbook/
    * 别人的资料（笔记代码）
        * [zhangxiann/Pytorch](https://github.com/zhangxiann/PyTorch_Practice)
* 生信
    * [B站生信技能书](https://www.bilibili.com/video/BV1cs411j75B)
* 算法
    * LeetCode
        * [labuladong的算法小抄](https://github.com/labuladong/fucking-algorithm)

## 文档

* [版本更新](docs/version.md)