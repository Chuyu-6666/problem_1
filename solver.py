"""
solver.py

功能：
-------
负责整个药材预热过程的时间推进。

调用:
heat_transfer.py
moisture_transfer.py

完成:
T^n,C^n -> T^(n+1),C^(n+1)

"""


import numpy as np



def solve(
        T0,
        C0,
        geometry,
        get_environment,
        params):


    # 初始状态

    T = T0.copy()

    C = C0.copy()


    # 保存历史

    T_history=[]
    C_history=[]
    time=[]



    for n in range(params.Nt):


        t=n*params.dt


        # 1. 获取外界条件

        Ta,Ca=get_environment(t)



        # 2. 温度更新

        T_new = update_temperature(
            T,
            Ta,
            geometry,
            params
        )


        # 3. 水分更新

        C_new = update_concentration(
            C,
            Ca,
            geometry,
            params
        )


        # 更新

        T=T_new
        C=C_new



        # 保存

        T_history.append(T.copy())
        C_history.append(C.copy())
        time.append(t)



    return (
        np.array(time),
        np.array(T_history),
        np.array(C_history)
    )