import numpy as np
import matplotlib.pyplot as plt


#------Simulation Parameters--------#
iterMax = 5000
iterNum = 0

gsize = 200 #Network size
fraction = .90 #Fraction of Network that is intialized in down state, rest in up state
numNOnes = int(np.floor((gsize**2)*fraction)) #Literally the number of negative ones

k = 1 #Make this unity because we are lazy 
startT = .5;endT = 5;stepT = .5; #These values define the array we are going to investigate for temperatures
numT = (endT-startT)/stepT+1 #Number of steps taken along temperatures
arrT = np.linspace(startT,endT,numT) #The actual array of temperatures

#------Generate Initial State Matrix--------#
#One way to generate state Matrix:
#statMat = np.random.randint(2,size=[gsize,gsize])*2-1

#We will use this clunky one though 
arrOnes = np.array(np.ones((gsize**2 - numNOnes))).flatten()
arrNOnes = np.ones(numNOnes)*-1
arrindex = np.hstack((arrOnes,arrNOnes))

statMat = np.random.permutation(arrindex)
statMat = np.reshape(statMat,[gsize,gsize])
statMatflip = np.copy(statMat) #Going to be the same matrix with a flipped state

statsT = [] #Where we will store the average Magnetization for a given Temperature
statsB = int(np.floor(iterMax*.9));statsE = iterMax #Beginning & End of Magnetiz. array we will use for stats

plt.figure()
for T in arrT:
    M = [] #Magnetization array for a given temperature
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

        #Conditions for a wrap-around environment, they are so cute!
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
        
        #Form the cross-hair for the state you are targeting
        coordNeighbors = [[xcor_m,ycor],[xcor_p,ycor],[xcor,ycor_m],[xcor,ycor_p]]
            
        #Sum the energies over the cross-hair
        for coords in coordNeighbors: 
            energy += statMat[coords[0],coords[1]]*statMat[xcor,ycor]
            energyflip += statMatflip[coords[0],coords[1]]*statMatflip[xcor,ycor]
            
        #-----Generate a Random number xchi so you can compare it to the change in energy-----#
        xchi = (np.random.random(1))
        energy = -energy/2
        energyflip = -energyflip/2

        Magnetization = np.abs(float(np.sum(np.sum(statMat)))/(gsize**2))  #Calculate the Magnetiation
        M.append(Magnetization)  #Store the magnetization at this iteration step

        #-----Implement the Metropolis algorithm to handle all of the dirty work----------#
        deltaE = energyflip-energy
        print('Energy,Energyflip: '+str(energy)+','+str(energyflip))
        if float(deltaE) < 0:
            statMat = np.copy(statMatflip)
            print('deltaE 1: ' +str(deltaE))
            print('flipped it')
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
    iterNum = 0 #Reset the iteration counter
    passT = np.copy(sum(M[statsB:(statsE-1)])/(statsE-statsB)) #Calculate the mean magnetiz. for this temp.
    statsT.append(passT) #Store the mean magnetiz. for this temp.


plt.figure()
plt.plot(arrT,statsT)
plt.title('Magnetization vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.show()


