import matplotlib.pyplot as plt
import numpy as np

#Need to parse data
f=open('/Users/darrellstepter/repos/school/NE204/Lab 0/dvstepter-lab0/lab0_spectral_data.txt')
lines=f.readlines()[1:]


Am241=[] # 59.54 keV
Ba133=[] # 80.997 keV (34%) 302.853 keV (18%) 356.017 keV (62%)
Cs137=[] # 661.66 keV
Co60=[] # 1173.2 keV and 1332.51 keV
Eu152=[] # 344.28 keV (27%) 1112.1 keV (14%) 1408.1 keV (21%) 121.78 keV (26%)
