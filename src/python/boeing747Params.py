class Params():
    def __init__(self):

        self.alt = 20000 #ft
        self.mach = 0.65
        self.g = 32.174 # ft/s2
        self.tas = 673 # ft/s
        self.rho = 0.0407 # lb/ft3
        self.dynPres = 287.2 # lb/ft2
        self.weight = 636636 # lb
        self.S = 5500 # ft2
        self.b = 196 # ft
        self.c = 27.3 # ft
        self.cg = 0.25 # 25% of c
        self.alpha = 2.5 # deg
        self.Ixx = 1.82e7 # slug-ft2
        self.Iyy = 3.31e7 # slug-ft2
        self.Izz = 4.97e7 # slug-ft2
        self.Ixz = -4.055; # slug-ft2

        # Longitudinal Derivatives
        self.Xu = -0.0059 # 1/s
        self.Xalpha = 15.9787 # ft/s2
        self.Zu = -0.1104 # 1/s
        self.Zalpha = -353.52 # ft/s2
        self.Mu = 0.0000 # 1/ft.s
        self.Malpha = -1.3028 # 1/s2
        self.Malphadot = -0.1057 # 1/s
        self.Mq = -0.5417 # 1/s
        self.XdelE = 0 # ft/s2
        self.ZdelE = -25.5659 # ft/s2
        self.MdelE = -1.6937 # 1/s2

        # Lateral-Directional Derivatives
        self.Ybeta = -71.9142 # ft/s2
        self.Lbeta = -2.7255 # 1/s2
        self.Lp = -0.8434 # 1/s
        self.Lr = 0.3224 # 1/s
        self.Nbeta = 0.9962 # 1/s2
        self.Np = -0.0236 # 1/s
        self.Nr = -0.2539 # 1/s
        self.YdelR = 9.5872 # ft/s2
        self.LdelR = 0.1363 # 1/s2
        self.NdelR = -0.6226 # 1/s2
        self.YdelA = 1.0386 # ft/s2
        self.LdelA = 0.2214 # 1/s2
        self.NdelA = 0.0112 # 1/s2