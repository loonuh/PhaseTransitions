import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------#
#   Set global variables and make Magnetization container
#----------------------------------------------------------------------#
SIZE = 150
STEPS = 10000
fraction = .9
statisticsFraction = .1
Mag = []
MagT = []
#----------------------------------------------------------------------#
#   Check periodic boundary conditions 
#----------------------------------------------------------------------#
def bc(i):
    if i+1 > SIZE-1:
        return 0
    if i-1 < 0:
        return SIZE-1
    else:
        return i

#----------------------------------------------------------------------#
#   Calculate internal energy
#----------------------------------------------------------------------#
def energy(system, N, M):
    return -1 * system[N,M] * (system[bc(N-1), M] 
                               + system[bc(N+1), M] 
                               + system[N, bc(M-1)] 
                               + system[N, bc(M+1)])

#----------------------------------------------------------------------#
#   Build the system
#----------------------------------------------------------------------#
def build_system():
    system = np.random.random_integers(0,1,(SIZE,SIZE))
    system[system==0] =- 1
    
    arrOnes = np.ones(SIZE**2-np.floor(fraction*SIZE**2))
    arrNOnes = np.ones(np.floor(fraction*SIZE**2))
    tmpSys = np.copy(np.hstack((arrOnes,arrNOnes)))
    
    system = np.reshape(tmpSys,[SIZE,SIZE])
    return system

#----------------------------------------------------------------------#
#   The Main monte carlo loop
#----------------------------------------------------------------------#
def main(T):
    system = build_system()
    print(system)
    for step, x in enumerate(range(STEPS)):
        M = np.random.randint(0,SIZE)
        N = np.random.randint(0,SIZE)

        E = -2. * energy(system, N, M)

        if E <= 0.:
            system[N,M] *= -1
        elif np.exp(-1./T*E) > np.random.rand():
            system[N,M] *= -1

        Mag.append(float(np.sum(system))/SIZE**2)
    return system
#----------------------------------------------------------------------#
#   Run the menu for the monte carlo simulation
#----------------------------------------------------------------------#
def run(T):
    print '='*70
    print '\tMonte Carlo Statistics for an ising model with'
    print '\t\tperiodic boundary conditions'
    print '='*70

    print "Choose the temperature for your run (0.1-100)"
    T = T
    data = main(T)
    return data

startT = .5;endT = 4;stepT = .25; #These values define the array we are going to investigate for temperatures
numT = (endT-startT)/stepT+1 #Number of steps taken along temperatures
arrT = np.linspace(startT,endT,numT) #The actual array of temperatures

plt.close("all")

for T in arrT:
    data=run(T)
    meanMag = np.mean(Mag[int(np.floor(np.size(Mag)*statisticsFraction)):(np.size(Mag)-1)])
    MagT.append(meanMag)
    Mag = []
    #plt.plot(Mag);
    plt.pcolor(data); plt.axis("tight");
    plt.title('Monty-Carlo Ising Model');
    plt.draw()

