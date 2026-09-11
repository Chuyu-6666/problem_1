import numpy as np

from config import dt, dr, hm,rho
def calculate_D(C):
    """
    Calculate moisture diffusion coefficient.

    Parameters
    ----------
    C : np.ndarray
        moisture concentration (kg/kg)

    Returns
    -------
    D : np.ndarray
        diffusion coefficient (m^2/s)
    """

    D = 7e-9 * np.exp(-0.89 /C)

    return D

def update_moisture(
        C,
        C_air,geometry,rho=rho

):
    """
    Calculate moisture concentration change in one time step.

    Parameters
    ----------
    C : np.ndarray
        Current moisture concentration of each control volume.
        shape: (N,)

    geometry : np.ndarray
        Geometry information.
        shape: (N,3)
        columns:
        [volume, inner_area, outer_area]

    D : float
        Moisture diffusion coefficient.
        unit: m^2/s

    C_air : float
        Moisture concentration of surrounding air.


    Returns
    -------
    dC : np.ndarray
        Moisture concentration change.
        shape: (N,)
    """
    D= calculate_D(C)



    N = len(C)


    # volume of each control volume
    V = geometry[:,0]

    # initialize moisture change
    C_new= np.zeros(N)


    # =========================
    # Internal control volumes
    # =========================

    for i in range(1, N-1):
        D_in=(D[i-1]+D[i])/2
        D_out=(D[i+1]+D[i])/2
        # inner flux
        J_in = -D_in * (C[i]-C[i-1]) / dr

        # outer flux
        J_out = -D_out * (C[i]-C[i+1]) / dr


        # areas
        A_in = geometry[i,1]
        A_out = geometry[i,2]


        C_new[i] = dt / (V[i]*rho) * (
            J_in*A_in
            +
            J_out*A_out
        )+C[i]


    # =========================
    # Center boundary
    # =========================

    # no moisture flux at center
    J_center = 0

    D_center_out=(D[i-1]+D[i])/2

    J_out = -D_center_out * (C[0]-C[1]) / dr

    A_out = geometry[0,2]


    C_new[0] = dt / (V[0]*rho)* (
        J_out*A_out
    )+C[0]


    # =========================
    # Surface boundary
    # =========================

    # moisture exchange with air
    D_surface_in=(D[-1]+D[-2])/2
    J_surface = hm * (C_air - C[-1])


    J_in = -D_surface_in * (C[-1]-C[-2]) / dr


    A_in = geometry[-1,1]

    A_surface = geometry[-1,2]


    C_new[-1] = dt / (V[-1]*rho) * (
        J_in*A_in
        +
        J_surface*A_surface
    )+C[-1]


    return C_new

if __name__ == '__main__':
    geometry = np.array([
        [1.0e-6, 0.0, 1.0e-4],
        [2.0e-6, 1.0e-4, 2.0e-4],
        [3.0e-6, 2.0e-4, 3.0e-4],
        [4.0e-6, 3.0e-4, 4.0e-4],
        [5.0e-6, 4.0e-4, 5.0e-4]
    ])
    C = np.array([
        2.55,
        2.55,
        2.55,
        2.55,
        2.55
    ])

    C_air = 0.5
    dC = calculate_moisture_change(
        C,
        C_air,geometry,rho=rho
    )

    print("dC:")
    print(dC)

