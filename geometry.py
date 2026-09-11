import numpy as np
import config
#要求：输入n（第几层），输出这一层的体积，外表面面积，内表面面积，以np列表的形式返回
#一次性将每一层的集合性质算出来 保存在一张列表里 下一次要用的时候直接查看
#creat_geometry[i](第几层)=【V，S_out,S_in】



def create_geometry():

    R=config.R
    L=config.L
    N=config.N


    dr=R/N


    V=[]
    S_in=[]
    S_out=[]


    for i in range(N):

        r_inner=i*dr
        r_outer=(i+1)*dr


        V_i=np.pi*L*(r_outer**2-r_inner**2)

        S_in_i=2*np.pi*r_inner*L

        S_out_i=2*np.pi*r_outer*L


        V.append(V_i)
        S_in.append(S_in_i)
        S_out.append(S_out_i)


    return V,S_in,S_out