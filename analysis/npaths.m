boggleAdjentMatrix
SumMatrix = zeros(16,16);
for n = 1:16
	SumMatrix+=boggleAdj^n;
end	
NPaths = sum(sum(SumMatrix));

disp(NPaths);
