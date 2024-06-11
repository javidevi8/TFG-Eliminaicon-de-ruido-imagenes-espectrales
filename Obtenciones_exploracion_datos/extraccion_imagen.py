import os
import numpy as np
import silx.io.utils as utils 
from silx.io import nxdata as nxdata
from matplotlib import pyplot as plt
import h5py

#Habrimos el fichero nxs para poder leer las imagenes
with h5py.File("015_sample_24_PrCo2P2.nxs", "r+") as original_file:
    print(utils.h5ls(original_file))
    #Accedemos a las primeras dimensiones de los datos
    dim1_2 =original_file["entry1/data/data"]

    #Accedemos al resto de dimensiones y las guardamos para extraer cada una de las imágenes
    print(dim1_2)
    dim0_2 = np.transpose(dim1_2, (1, 0, 2))
    dim0_1 = np.transpose(dim1_2, (2, 0, 1))
   

    lista_dimensiones = [dim1_2,dim0_2,dim0_1]
    # print(len(dim0_1))
    #Recorremos cada una de las dimensiones para extraer las imágenes
    for i in range(3):
        aux_dim = lista_dimensiones[i]
        for j in range(len(aux_dim)):
            imagen_nombre = f"{'dimension'+str(i)}_{j:03d}.png"
            plt.imsave(os.path.join("Datos/", imagen_nombre), aux_dim[j])



    original_file.close()
