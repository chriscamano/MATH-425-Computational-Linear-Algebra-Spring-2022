import numpy as np
import matplotlib.pyplot as plt
import transformations
from transformations import Transformations



data = np.load('letterN.npy')
N=Transformations(data)



#Render original 
plt.subplot(121),N.display()

N.translate(-2, 3)
N.stretch(.8,1.2)
#Part a
plt.subplot(121),N.display()

#reload data 
data = np.load('letterN.npy')
N=Transformations(data)

N.rotate(np.pi/6)
N.reflect(0,1)
#Part b
plt.subplot(121),N.display()