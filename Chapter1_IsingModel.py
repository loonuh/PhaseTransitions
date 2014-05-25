import numpy as np
import matplotlib.pyplot as plt

iterMax = 100
iterNum = 0

gsize = 32
numNOnes = 100

k = 1
startT = .5;endT = 5;stepT = .5;
numT = (endT-startT)/stepT+1
T = .5

arrT = np.linspace(startT,endT,numT)

statMat = np.random.randint(2,size=[gsize,gsize])*2-1

arrOnes = np.array(np.ones((gsize**2 - numNOnes))).flatten()
arrNOnes = np.ones(numNOnes)*-1
arrindex = np.hstack((arrOnes,arrNOnes))

#Reshaping statMat
statMat = np.random.permutation(arrindex)
statMat = np.reshape(statMat,[gsize,gsize])

print(np.size(statMat))
statMatflip = np.copy(statMat) 
plt.figure()
M = []

while iterNum < iterMax:
    iterNum += 1
    matMTemp = np.zeros([np.size(iterMax),np.size(arrT)])
    print('\n')
    print('Iteration:'+str(iterNum))
    
    xcor = np.random.randint(gsize)
    ycor = np.random.randint(gsize)
    statMatflip[xcor,ycor] = -statMat[xcor,ycor]
    energy = 0 
    energyflip = 0

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
        energyflip += statMatflip[coords[0],coords[1]]*statMatflip[xcor,ycor]
            
    xchi = (np.random.random(1))
    energy = -energy/2
    energyflip = -energyflip/2
    
    Magnetization = np.abs(float(np.sum(np.sum(statMat)))/(gsize**2))
    M.append(Magnetization)

    deltaE = energyflip-energy
    
    print('Energy,Energyflip: '+str(energy)+','+str(energyflip))
    if float(deltaE) < 0:
        statMat = np.copy(statMatflip)
        print('deltaE 1: ' +str(deltaE))
        print('flipped it')
    #elif deltaE == 0:
    #    print('no action')
    #    continue
    else:
        W = np.exp(-deltaE/T/k)
        if float(W) >= xchi:
            statMat=np.copy(statMatflip)
            print('deltaE 2: ' +str(deltaE))
            print('W,xchi: ' +str(W)+','+str(xchi))
            print('flipped it')
        else:
            statMat = np.copy(statMat)
            print('no action')
    if np.mod(iterNum,1) == 0:
        plt.pcolor(np.transpose(statMat))
        plt.axis("tight")
        plt.draw()

plt.figure()
plt.plot(M)
plt.draw()
plt.show()
