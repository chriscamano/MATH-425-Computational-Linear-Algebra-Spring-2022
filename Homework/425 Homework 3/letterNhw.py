import numpy as np
import matplotlib.pyplot as plt

data = np.load('letterN.npy')
mat1=data[0]
mat2=data[1]
mat1=mat1.reshape((3,3))
mat2=mat2.reshape((3,3))
LinearTransformation1=np.matrix([[1,0,-2],[0,1,3],[0,0,1]])
LinearTransformation2=np.matrix([[],[],[]])
plt.rcParams["figure.figsize"] = [7.00, 3.50] 
plt.rcParams["figure.autolayout"] = True

origin =[0,0,0]
fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(111, projection='3d')

def plotvects(x):
    color=['black','red','green']
    for i in range(3):
        ax.quiver(origin[0],origin[1],origin[2], mat1[0,i], mat1[1,i],mat1[2,i], color=color[i])
    return
#plotvects(mat1)
#plt.show()
plotvects(mat2)
plt.show()