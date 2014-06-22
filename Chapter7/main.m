

%1) Define system size
%2) Monte Carlo select on string: S_i
%3) Replicate S_i into S_j, i=/=j, with (f1,f2)
%4) Flip states of string with mutation rate, mu.

clear all
N = 300;
numSites = 16;
maxIterations = 10000;


%N = 10;
%numSites = 3;
%maxIterations = 1;

arrSites = cell([1,numSites]);

f1 = 1;
f2 = .25;

muB = .035;

% Build sample population
for I = 1:N
        arrSites{I} = ones(1,numSites);
end

for I = 1:maxIterations
    pickPair = randsample(1:N,2,'false');
    chi = rand(1);
    if sum(arrSites{pickPair(1)}) == numSites %This means its master sequence
        if chi < f1
             S_i_copy = copySite(pickPair(1),arrSites,muB,numSites);
             arrSites{pickPair(2)} = S_i_copy;
        end
    else %its not master so use f2
        if chi < f2
            S_i_copy = copySite(pickPair(1),arrSites,muB,numSites);
            arrSites{pickPair(2)} = S_i_copy;
        end
    end
    
    for Z = 1:N
        arrCount(I,Z) = sum(arrSites{Z});
    end
end

if 1
    for iter = 1:size(arrCount,1)
        for num = 1:numSites
            stats(iter,num) = length(find(arrCount(iter,:) == num));
        end
    end
end

for I = 1:numSites
    legendNames{I} = num2str(I)
end

%Plot species with mutations <= 4
plot(stats(1:25:10000,numSites-4:numSites)), hold all
legend(legendNames{numSites-4:numSites})