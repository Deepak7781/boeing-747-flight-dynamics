import control
import numpy as np
from boeing747Params import Params
from stateSpaceModel import stateSpace
p = Params()

lonSS, latSS = stateSpace(p)

Alon = lonSS.A
lonEigen = np.linalg.eig(Alon)
print(lonEigen.eigenvalues)

Alat = latSS.A
latEigen = np.linalg.eig(Alat)
print(latEigen.eigenvalues)