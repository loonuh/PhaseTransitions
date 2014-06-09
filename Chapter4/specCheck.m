function [burnCont,forest] = specCheck(forest)

[fireRow,fireCol] = find(forest == 2);
fire = [fireRow,fireCol];
burnCont = 0;

for treeFire = 1:size(fire,1)
    if forest(fire(treeFire,1)+1,fire(treeFire,2)) == 1
        forest(fire(treeFire,1)+1,fire(treeFire,2)) = 2;
        burnCont =1;
    end
    
    if forest(fire(treeFire,1)-1,fire(treeFire,2)) == 1
        forest(fire(treeFire,1)-1,fire(treeFire,2)) = 2;
        burnCont =1;
    end
    
    if forest(fire(treeFire,1),fire(treeFire,2)-1) == 1
        forest(fire(treeFire,1),fire(treeFire,2)-1) = 2;
        burnCont =1;
    end
    
    if forest(fire(treeFire,1),fire(treeFire,2)+1) == 1
        forest(fire(treeFire,1),fire(treeFire,2)+1) = 2;
        burnCont =1;
    end
end
end

