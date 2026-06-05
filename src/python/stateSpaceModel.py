import numpy as np
import control
def stateSpace(ac):

    Alon = np.array([[ac.Xu, ac.Xalpha, 0, -ac.g],
                     [ac.Zu/ac.tas, ac.Zalpha/ac.tas, 1, 0], 
                     [ac.Mu+(ac.Malphadot*ac.Zu/ac.tas), ac.Malpha+(ac.Malphadot*ac.Zalpha/ac.tas), ac.Mq+ac.Malphadot, 0],
                     [0, 0, 1, 0]])

    Blon = np.array([[ac.XdelE], [ac.ZdelE/ac.tas], [ac.MdelE+(ac.Malphadot*ac.ZdelE/ac.tas)],  [0]]);

    Clon = np.eye(4);
    Dlon = np.zeros((4,1));

    lonSS = control.ss(Alon, Blon, Clon, Dlon)
    lonSS.state_labels = ['u[m/s]', 'alpha[rad]', 'q[rad/s]', 'theta[rad]']

    lonSS.input_labels = ['delta_e[rad]']

    lonSS.output_labels = ['u[m/s]', 'alpha[rad]', 'q[rad/s]', 'theta[rad]']

    Alat = np.array([[ac.Ybeta/ac.tas, 0, -1, ac.g/ac.tas],
            [ac.Lbeta, ac.Lp, ac.Lr, 0], 
            [ac.Nbeta, ac.Np, ac.Nr, 0],
            [0, 1, 0, 0]])
    
    Blat = np.array([[ac.YdelA/ac.tas,ac.YdelR/ac.tas],
            [ac.LdelA, ac.LdelR],
            [ac.NdelA, ac.NdelR],
            [0,0]])

    Clat = np.eye(4);

    Dlat = np.zeros((4,2));

    latSS = control.ss(Alat, Blat, Clat, Dlat);
    latSS.state_labels = ['v[m/s]', 'p[rad/s]', 'r[rad/s]', 'phi[rad]']

    latSS.input_labels = ['delta_a[rad]', 'delta_r[rad]']

    latSS.output_labels = ['v[m/s]', 'p[rad/s]', 'r[rad/s]', 'phi[rad]']
    return lonSS, latSS
