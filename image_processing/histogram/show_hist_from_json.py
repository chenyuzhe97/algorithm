# -*- encoding: utf-8 -*-
"""
@File Name      :   show_hist_from_json.py    
@Create Time    :   2022/9/1 15:44
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

import json

import click
from matplotlib import pyplot as plt


@click.command()
@click.argument('json_path', type=click.Path(exists=True))
def main(json_path: str):
    hist_distribution = json.load(open(json_path, 'r'))
    for color, distribution in hist_distribution.items():
        distribution = [val for key, val in distribution.items()]
        plt.plot(distribution, color)
    plt.xlim([0, 256])
    plt.title("image2")
    plt.show()


if __name__ == '__main__':
    """
    从JSON文件读取数据展示直方图
    """
    main()
