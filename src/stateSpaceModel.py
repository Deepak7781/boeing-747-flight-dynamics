import numpy as np
import control
def stateSpace(ac):

    Alon = np.array([[ac.Xu, ac.Xalpha, 0, -ac.g],
                     [ac.Zu/ac.tas, ac.Zalpha/ac.tas, 1, 0], 
                     [ac.Mu+(ac.Malphadot*ac.Zu/ac.tas), ac.Malpha+(ac.Malphadot*ac.Zalpha/ac.tas), ac.Mq+ac.Malphadot, 0],
                     [0, 0, 1, 0]])

    Blon = np.array([[ac.XdelE], [ac.ZdelE/ac.tas], [ac.MdelE+(ac.Malphadot*ac.ZdelE/ac.tas)],  0]);

    Clon = np.eye(4);
    Dlon = np.zeros(4,1);

    lonSS = control.ss(Alon, Blon, Clon, Dlon)
    lonSS.StateName = {'u[m/s]', '\alpha[rad]', 'q[rad/s]', '\theta[rad]'};
    lonSS.InputName = {'\delta_e[rad]'};
    lonSS.OutputName = {'u[m/s]', '\alpha[rad]', 'q[rad/s]', '\theta[rad]'};