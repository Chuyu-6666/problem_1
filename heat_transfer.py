import numpy as np

from config import dt, rho, cp, k, h, dr






def calculate_temperature_change(T, T_air, geometry,k=k,rho=rho,cp=cp):

    N = len(T)

    dT = np.zeros(N)


    V = geometry[:,0]
    S_in = geometry[:,1]
    S_out = geometry[:,2]


    # center layer
    Q_out = k*S_out[0]*(T[1]-T[0])/dr

    dT[0] = dt/(rho*cp*V[0])*(-Q_out)


    # inner layers
    for i in range(1,N-1):

        Q_in = k*S_in[i]*(T[i-1]-T[i])/dr

        Q_out = k*S_out[i]*(T[i+1]-T[i])/dr

        dT[i] = dt/(rho*cp*V[i])*(Q_in-Q_out)



    # surface layer
    Q_in = k*S_in[-1]*(T[-2]-T[-1])/dr

    Q_surface = h*S_out[-1]*(T_air-T[-1])


    dT[-1] = dt/(rho*cp*V[-1])*(Q_in+Q_surface)


    return dT