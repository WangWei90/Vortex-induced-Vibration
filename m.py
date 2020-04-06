## =================================================================== ##
#  this is file mef-calor1d.py, created at 30-May-2019                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##

import numpy as np
import meshio



import meshio



# definicao das constantes do problema
nu = 1
dt = 0.0001

velini=200.0 #velocidade inicial

msh = meshio.read("mo.msh")
test = meshio.read("mo.msh")
X = msh.points[:,0]
Y = msh.points[:,1]
Z = test.points[:,1]
xyz = msh.points


IEN = msh.cells_dict["triangle"]
cells=[('triangle',IEN)]


cc = msh.cells_dict["line"]
cc.reshape((cc.size)) # reshape for line vector
cc.sort()
cc = np.unique(cc)
cc2=[]
cc3=[]
for i in range(0,len(Y)):
    if Y[i]< 5 and Y[i] > -5 and X[i]< 5 and X[i] > -5:
        cc2.append(i)
    if Y[i]< 0.501 and Y[i] > -0.501 and X[i]< 0.501 and X[i] > -0.501:
        cc3.append(i)
        #print(i)
for INTE in range(0,100):

    for i in cc2:
        Y[i] = Z[i]+ np.sin(INTE/10.0)/(np.absolute(Y[i])+2+np.absolute(X[i]))
        xyz[i]=[X[i],Y[i],0.0]
    for i in cc3:
        Y[i] = Z[i]+np.sin(INTE/10.0)/2.5


    meshio.write_points_cells(
    "inte{}.vtk".format(INTE),
    xyz,
    cells
    )
