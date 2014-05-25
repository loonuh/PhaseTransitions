import numpy as np
import matplotlib.pyplot as plt

iterMax = 1000
iterNum = 0

gsize = 16
#numZeros = 3

k = 1
startT = .5;endT = 5;stepT = .5;
numT = (endT-startT)/stepT+1
T = .5

arrT = np.linspace(startT,endT,numT)

statMat = np.random.randint(2,size=[gsize,gsize])*2-1
print(np.size(statMat))
statMatflip = np.copy(statMat) 
plt.figure()
M = []

while iterNum < iterMax:
    iterNum += 1
    matMTemp = np.zeros([np.size(iterMax),np.size(arrT)])
    print('\n')
    print('Iteration:'+str(iterNum))
    
    xcorflip = np.random.randint(gsize)
    ycorflip = np.random.randint(gsize)
    statMatflip[xcorflip,ycorflip] = -statMat[xcorflip,ycorflip]
    
    energy = 0 
    energyflip = 0

    energyS = np.zeros([gsize,gsize])
    energySflip = np.zeros([gsize,gsize])

    for xcor in range(gsize):
        for ycor in range(gsize):
            if xcor == gsize-1:
                xcor_p = 0
            else:
                xcor_p = xcor+1
            if xcor == 0:
                xcor_m = gsize-1
            else:
                xcor_m = xcor-1
            if ycor == gsize-1:
                ycor_p = 0
            else:
                ycor_p = ycor+1
            if ycor == 0:
                ycor_m = gsize-1
            else:
                ycor_m = ycor-1
            
            coordNeighbors = [[xcor_m,ycor],[xcor_p,ycor],[xcor,ycor_m],[xcor,ycor_p]]
            for coords in coordNeighbors: 
                energy += statMat[coords[0],coords[1]]*statMat[xcor,ycor]
                energyS[xcor,ycor] += statMat[coords[0],coords[1]]*statMat[xcor,ycor]
                
                energySflip[xcor,ycor] += statMatflip[coords[0],coords[1]]*statMatflip[xcor,ycor]
                energyflip += statMatflip[coords[0],coords[1]]*statMatflip[xcor,ycor]
            
    xchi = (np.random.random(1))
    energy = -energy/2
    energyflip = -energyflip/2
    
    Magnetization = np.abs(float(np.sum(np.sum(statMat)))/(gsize**2))
    M.append(Magnetization)
    deltaE = energyflip-energy
    
    print('Energy,Energyflip: '+str(energy)+','+str(energyflip))
    if deltaE < 0:
        statMat = np.copy(statMatflip)
        print('flipped it')
    else:
        W = np.exp(-deltaE/T/k)
        if float(W) <= xchi:
            statMat=np.copy(statMatflip)
            print('flipped it')
        else:
            statMat = np.copy(statMat)
            print('no action')
    if np.mod(iterNum,100) == 0:
        plt.pcolor(np.transpose(statMat))
        plt.axis("tight")
        plt.draw()

plt.figure()
plt.plot(M)
plt.show()
