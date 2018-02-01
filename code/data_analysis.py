import matplotlib.pyplot as plt
import numpy as np

#Need to parse data
f=open('/Users/darrellstepter/repos/school/NE204/Lab0/dvstepter-lab0/lab0_spectral_data.txt')
lines=f.readlines()[1:]


Am241=[] # 59.54 keV
Ba133=[] # 80.997 keV (34%) 302.853 keV (18%) 356.017 keV (62%)
Cs137=[] # 661.66 keV
Co60=[] # 1173.2 keV and 1332.51 keV
Eu152=[] # 344.28 keV (27%) 1112.1 keV (14%) 1408.1 keV (21%) 121.78 keV (26%)

for x in lines:
    x.split('\t')
    y=[int(s) for s in x.split() if s.isdigit()]
    Am241.append(y[0])
    Ba133.append(y[1])
    Cs137.append(y[2])
    Co60.append(y[3])
    Eu152.append(y[4])
# testing that input vectors have the same length
f.close()

chan=list(range(1,len(Cs137)+1)) #number of channels:8192

centroid_Cs=np.argmax(Cs137) # 661.66 keV
centroid_Am=np.argmax(Am241) # 59.54 keV

x1=centroid_Am
x2=centroid_Cs

y1=59.5409
y2=661.657

energies=[]
m=float(y2-y1)/(x2-x1)
b=float(-m*x1+y1)
print(m,b)

chan_array=np.array(chan)

for i in chan:
    energies.append(np.multiply(m, chan_array[i-1])+b)


plt.semilogy(chan, Am241,chan, Ba133,chan, Cs137, chan,Co60, chan, Eu152) #Makes raw data plot
plt.title('Raw Data')
plt.xlabel('Channel Number')
plt.ylabel('Counts')
plt.savefig('/Users/darrellstepter/repos/school/NE204/Lab0/dvstepter-lab0/images/Raw_Spec.png')
plt.show()
