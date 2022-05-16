# 用于学习和测试算法的项目

<p align="center">
<a href="https://github.com/diklios5768" target="_blank">
<img alt="Github" src="https://img.shields.io/badge/作者-@diklios-000000.svg?style=flat-square&logo=GitHub">
</a>
<a href="https://github.com/diklios5768/algorithm" target="_blank">
<img alt="GitHub" src="https://img.shields.io/github/stars/diklios5768/algorithm?label=Stars&style=flat-square&logo=GitHub">
</a>
</p>

## 说明

- 本项目包含了大量常用的基础库、算法、机器学习和深度学习库，还有自己的算法文件，安装所有的环境会占用**4-8GB**以上的空间，**请酌情考虑是否要全部安装**
  - 在`Pipfile`或者`conda.yaml`文件中注释不需要的库即可大幅度减少体积

## 安装环境

### 使用 pipenv 管理环境

---

- 由于使用原生的 CPython，安装的包因为大多数是源码，本机编译出来的环境会比 conda 要小一些，但是要保证编译环境正常
- 安装 python（推荐 _3.6_ 以上的版本，且附带 pip）
- 在终端中输入：`pip install pipenv`
  - q 请检查自己的网络情况，在国内的话尽量能够使用代理，否则非常慢
  - 如果不方便使用代理，请百度`pip`换源教程，把`pipenv`包安装上就行
  - 最后在`Pipfile`文件中注释`pypi`源的内容，换为任意一个国内的源（即取消注释）
- 设置`Pipfile`
  - 本项目默认是 python3.9 版本，可以在文件最后的`python_version`部分修改为你安装的版本
- 设置环境变量
  - 创建`.env`文件（因为文件中可能会包含敏感信息，建议永远不要传到公开的仓库中）
  - 文件内容参考如下：

```dotenv
#让环境创建在当前项目目录下，否则默认是用户文件夹下的.virtualenvs文件夹
PIPENV_VENV_IN_PROJECT=1
#保持其他包不更新，因为pipenv install/update 会默认更新所有包
PIPENV_KEEP_OUTDATED=1
#默认不清除缓存
PIPENV_CLEAR=0
```

- 检查自己的编译环境
  - 请安装`c++ build tools 14`以上的版本
    - 一般在安装报错的终端提示中会有链接
    - 可以使用微软官方包管理工具`winget`安装
    - 可以直接安装 visual studio 2017 以上的版本，选择 c++开发环境即可
- 进入到当前项目文件夹，运行命令：`pipenv install`

### 使用 Conda 管理环境

---

- 安装 conda
  - 从官网下载 anaconda3 或者 miniconda3
  - 使用 scoop 安装 anaconda3 或者 miniconda3（不要使用 dorado 库，有问题）
- 创建环境
  - `conda env create -f conda.yaml`

## 激活环境

### Pipenv

- `pipenv shell`
- 如果不想新建一个终端：`pipenv run 命令`
- 一些 IDE 也拥有选择环境的方法

### Conda

- `conda activate algorithm`

## 参考资料

- 机器学习和深度学习
  - GitHub 项目
    - [ML-notes](https://github.com/Sakura-gh/ML-notes)
    - [AI learning](https://github.com/apachecn/AiLearning)
    - [斯坦福大学 2014（吴恩达）机器学习教程中文笔记](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes)
    - [动手学深度学习](https://github.com/d2l-ai/d2l-zh)
      - [《动手学深度学习》PyTorch 代码实现](https://github.com/ShusenTang/Dive-into-DL-PyTorch)
        - <https://tangshusen.me/Dive-into-DL-PyTorch>
      - [《动手学深度学习》TensorFlow2.0 代码实现](https://github.com/TrickyGo/Dive-into-DL-TensorFlow2.0)
        - <https://trickygo.github.io/Dive-into-DL-TensorFlow2.0>
      - 李沐的《动手学深度学习》在线版
        - <http://zh.d2l.ai/>
        - <https://zh-v2.d2l.ai/>
  - 课程
    - [吴恩达机器学习系列课程](https://www.bilibili.com/video/BV164411b7dx)
    - [李宏毅 2020 版机器学习深度学习](https://www.bilibili.com/video/BV1JE411g7XF)
    - [李宏毅《机器学习/深度学习》2021 版课程](https://www.bilibili.com/video/BV1JA411c7VT)
    - [吴恩达深度学习](https://www.bilibili.com/video/BV1FT4y1E74V)
  - 书籍
    - 周志华的《机器学习》
    - 神经网络与深度学习，邱锡鹏，在线版：<https://nndl.github.io/>
    - 《深度学习》（花书）
    - [机器学习基础在线版](https://mitpress.ublish.com/ereader/7093/?preview=#page/1)
      - 下载 PDF：<https://cs.nyu.edu/~mohri/mlbook/>
    - [《机器学习公式推导及代码实现》的代码](https://github.com/luwill/Machine_Learning_Code_Implementation)
  - 别人的资料（笔记、代码）
    - [zhangxiann/Pytorch](https://github.com/zhangxiann/PyTorch_Practice)
  - 学习过程参考
    - [深度学习如何入门](https://www.zhihu.com/question/26006703/answer/536169538)
- 生信
  - [B 站生信技能书](https://www.bilibili.com/video/BV1cs411j75B)
- 算法
  - LeetCode
    - [labuladong 的算法小抄](https://github.com/labuladong/fucking-algorithm)

## 文档

- [更新记录](docs/changelog.md)

## 待完成

- numpy、pandas 等学习内容更改为 jupyter notebook 文件
