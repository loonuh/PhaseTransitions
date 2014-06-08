clear all
close all

%------------------------------------------------------------%
%            Welcome to Percolation by Chris Luna!           %
%------------------------------------------------------------%

% In this simulation of percolation, the trees at the bottom of
% the grid are set on fire and the fire will spread over the 
% L by L grid that contains a percentage of its elements, p,
% that have been filled with trees.

%------------------------------------------------------------%
%                        INSTRUCTIONS                        %
%------------------------------------------------------------%

%1) Before beginning, make sure that you download dataL.txt, and
%   burnCheck.m!!!
%
%2) Set L as the grid size, the grid will be L by L.
%   Leave L at 100 when beginning.
%
%3) Set percentage, p, of matrix that will be 'trees'. Set this
%   to be larger than .6 if you are using Case = 2.
%
%4) Choose to run either Case = 1 or Case 2. Case = 1 is the
%   basic case of percolation.
%
%5) We you are ready, click run!

L = 500; %Grid size, 100 is a good default
p = .6; %Initial Percentage, set p>.6 when using Case = 2
Case = 1; %Select a value for 'Case', either Case = 1 or Case = 2
Video = 1; %Do you want to make a video? Set Video = 0/1 ('off'/'on')
%--------------------Dynamics For Percolation---------------------%
if Video
    vidObj = VideoWriter('Percolation.avi');
    open(vidObj);
end

arrDataOnes = ones(1,floor(L*L*p));
arrDataZeros = zeros(1,L*L - length(arrDataOnes));
arrData = [arrDataOnes arrDataZeros];

indx = randperm(length(arrData));
arrData = arrData(indx);
matData = reshape(arrData,[L,L]);

forest = matData;
forest = [zeros(length(forest),1),forest,zeros(length(forest),1)];
forest = [zeros(1,length(forest));forest;zeros(1,length(forest))];

trees = find(forest(2,:) == 1);

if Case == 1
    %Do  nothing
elseif Case == 2
    Y = load('dataL.txt');
    %Y = -(Y-1)
    forest([floor(L/2)-4:floor(L/2)+8-4],[floor(L/2)-4:floor(L/2)+10-4]) = Y;
end

forest(2,trees) = 2;
burnCont = burnCheck(forest);
while burnCont == 1
    [burnCont,forest] = burnCheck(forest);pcolor(forest(2:end-1,2:end-1));
    nameTitle = strcat(['Percolation, p = ',num2str(p),', grid = ',num2str(L),' x ',num2str(L)]);
    title(nameTitle)
    shading flat;
    drawnow;
    if Video
        writeVideo(vidObj,getframe(gcf));
    end
end

if Video
    close(vidObj);
end
