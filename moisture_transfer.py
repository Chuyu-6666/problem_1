"""
moisture_transfer.py


功能：
------
根据当前药材内部水分浓度分布，
计算下一时间步的水分浓度。


输入：
------
C:
    numpy.ndarray
    shape=(N,)
    当前水分浓度分布


Ca:
    float
    外界空气水分浓度


V:
    numpy.ndarray
    shape=(N,)
    控制体体积


A:
    numpy.ndarray
    shape=(N-1,)
    控制体间界面面积


As:
    float
    药材外表面积


D:
    水分扩散系数


hm:
    水分传递系数


dt:
    时间步长


输出：
------
C_new:
    numpy.ndarray
    shape=(N,)

    下一时刻水分浓度分布


数学模型：
------
Fick扩散定律：

J=-D*dC/dr


质量守恒：

V*dC/dt
=
J_in*A_in-J_out*A_out

"""