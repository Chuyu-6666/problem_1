
#要求：输入n（第几层），输出这一层的体积，外表面面积，内表面面积，以np列表的形式返回
#一次性将每一层的集合性质算出来 保存在一张列表里 下一次要用的时候直接查看
#creat_geometry[i](第几层)=【V，S_out,S_in】

import numpy as np
from config import R, L


def generate_geometry(N):

    dr = R / N

    geometry = np.zeros((N,3))


    for i in range(N):

        # 第 i+1 层
        r_in = i * dr
        r_out = (i+1) * dr


        # volume
        V = np.pi*(r_out**2-r_in**2)*L


        # inner surface
        S_in = 2*np.pi*r_in*L


        # outer surface
        S_out = 2*np.pi*r_out*L


        geometry[i] = [
            V,
            S_in,
            S_out
        ]


    return geometry

