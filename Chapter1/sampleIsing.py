import numpy as np
import sys
#----------------------------------------------------------------------#
#   Check periodic boundary conditions 
#----------------------------------------------------------------------#
def bc(i,SIZE):
    if i+1 > SIZE-1:
        return 0
    if i-1 < 0:
        return SIZE-1
    else:
        return i

#----------------------------------------------------------------------#
#   Calculate internal energy
#----------------------------------------------------------------------#
def energy(system, N, M,SIZE):
    return -1 * system[N,M] * (system[bc(N-1,SIZE), M] 
                               + system[bc(N+1,SIZE), M]
                               + system[N, bc(M-1,SIZE)]
                               + system[N, bc(M+1,SIZE)])

#----------------------------------------------------------------------#
#   Build the system
#----------------------------------------------------------------------#
def build_system(SIZE,STEPS):
    system = np.random.random_integers(0,1,(SIZE,SIZE))
    system[system==0] =- 1

    return system

#----------------------------------------------------------------------#
#   The Main monte carlo loop
#----------------------------------------------------------------------#
def rmain(T,SIZE,STEPS):
    system = build_system(SIZE,STEPS)

    for step, x in enumerate(range(STEPS)):
        M = np.random.randint(0,SIZE)
        N = np.random.randint(0,SIZE)

        E = -2. * energy(system, N, M,SIZE)

        if E <= 0.:
            system[N,M] *= -1
        elif np.exp(-1./T*E) > np.random.rand():
            system[N,M] *= -1

#----------------------------------------------------------------------#
#   Run the menu for the monte carlo simulation
#----------------------------------------------------------------------#
def run():
    print '='*70
    print '\tMonte Carlo Statistics for an ising model with'
    print '\t\tperiodic boundary conditions'
    print '='*70

    print "Choose the temperature for your run (0.1-100)"
    T = float(2.2)

    print "Choose your system SIZE:"
    SIZE = int(10)

    print "Choose your system SIZE:"
    STEPS = int(50)

    rmain(T,SIZE,STEPS)



if __name__ == "__main__":
    run()

