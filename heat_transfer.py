import numpy as np

from config import dt, rho, cp, k, h, dr






def update_temperature(T, T_air, geometry,k=k,rho=rho,cp=cp):

    N = len(T)

    dT = np.zeros(N)


    V = geometry[:,0]
    A_in = geometry[:,1]
    A_out = geometry[:,2]


    # center layer
    Q_out = k*A_out[0]*(T[1]-T[0])/dr

    dT[0] = dt/(rho*cp*V[0])*Q_out


    # inner layers
    for i in range(1,N-1):

        Q_in = -k*A_in[i]*(T[i]-T[i-1])/dr

        Q_out = -k*A_out[i]*(T[i]-T[i+1])/dr

        dT[i] = dt/(rho*cp*V[i])*(Q_in+Q_out)



    # surface layer
    Q_in = k*A_in[-1]*(T[-2]-T[-1])/dr

    Q_surface = h*A_out[-1]*(T_air-T[-1])


    dT[-1] = dt/(rho*cp*V[-1])*(Q_in+Q_surface)


    T_new=T+dT

    return T_new