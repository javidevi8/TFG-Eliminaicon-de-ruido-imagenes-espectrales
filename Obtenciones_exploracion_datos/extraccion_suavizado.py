import os
import numpy as np
import silx.io.utils as utils 
from silx.io import nxdata as nxdata
from matplotlib import pyplot as plt
from skimage.restoration import denoise_tv_chambolle
import h5py



with h5py.File("001_sample_24_PrCo2P2.nxs", "r+") as original_file:
    #Mostramos el contenido del archivo.
    print(utils.h5ls(original_file))
    data =original_file["entry1/data/data"]

    img = np.array(data)

    plt.imshow(img, cmap='viridis') 
    plt.gca().invert_yaxis()
    plt.title('Imagen de ejemplo')
    plt.show()

    #Suavizado de prueba
    denoised_img = denoise_tv_chambolle(img, weight=0.1, channel_axis = 3) 
    plt.imshow(denoised_img)
    plt.title('Denoised Image')
    plt.show()

    original_file.close()

    plt.imsave(os.path.join("Datos_prueba/", "ImagenSucia2.png"),img )
    plt.imsave(os.path.join("Datos_prueba/", "ImagenLimpia.png"),denoised_img )

with h5py.File("001_sample_24_PrCo2P2.nxs", "r+") as original_file:

    # Comprobamos si se puede introducir la nueva imagen en el archivo
    original_file["entry1/data/data"] = denoised_img  

    original_file.close()


input("press something...")