function [S_i_copy] = copySite(S_i,arrSites,muB,numSites)

arrChi = rand(1,numSites)
ind = find(arrChi < muB)

tmp = arrSites{S_i}
tmp(ind) = 1 - arrSites{S_i}(ind)
S_i_copy = tmp

end

