from boeing747Params import Params
from stateSpaceModel import stateSpace
p = Params()

lonSS, latSS = stateSpace(p)
print(lonSS)

print(latSS)
