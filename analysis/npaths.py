from oct2py  import octave
from numpy import matrix
from numpy import linalg
from numpy import ma
from numpy import sum
#script ouputs possible combos of boggle board
#arbitrary point arithmetic is nice
octave.addpath('.')
octave.eval('boggleAdjentMatrix')
AdjentMatrix = octave.pull('boggleAdj')
AdjentMatrix = matrix(AdjentMatrix)

SumAdjentMatrix = matrix(ma.zeros((16,16),dtype=int))

for n in range(3s,16+1): #valid boggle words start at three
	SumAdjentMatrix+=AdjentMatrix**n
	
NPaths = sum(SumAdjentMatrix)
print(NPaths)
