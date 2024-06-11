
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from scipy import stats
from scipy.fft import fft2, fftshift


ruta_imagen = "Datos_prueba/dimension0_079.png"

# Carga la imagen
imagen = cv2.imread(ruta_imagen,cv2.IMREAD_GRAYSCALE)
print(imagen.shape)

# Carga la imagen
imagen2 = Image.open(ruta_imagen)

# Convierte la imagen a escala de grises
imagen_gris = imagen2.convert('L')

imagen_array = np.array(imagen_gris)

############################## Calcula el histograma #########################################
histograma = np.histogram(imagen_array, bins=256, range=(0, 256))[0]

# Muestra el histograma
plt.figure()
plt.title("Histograma de la imagen")
plt.xlabel("Valor de píxel")
plt.ylabel("Número de píxeles")
plt.plot(histograma, color='black')
plt.xlim([0, 256])
plt.yscale('log')
plt.show()

# Calcula la media y la desviación estándar
media = np.mean(imagen)
desviacion_estandar = np.std(imagen)

print("Media de la imagen:", media)
print("Desviación estándar de la imagen:", desviacion_estandar)

plt.imshow(imagen)
plt.show()

#############################################################################################

###########################Fourier#################################

# Tamaño de la imagen
N = 256

# Generar señal de ruido gaussiano
media_gauss = 0
desv_est_gauss = 10
ruido_gaussiano = np.random.normal(media_gauss, desv_est_gauss, size=(573, 846))

# Generar señal de ruido de Poisson
lambda_poisson = 10
ruido_poisson = np.random.poisson(lambda_poisson, size=(573, 846))

# Calcular la transformada de Fourier de cada ruido
fft_ruido_gaussiano = fft2(ruido_gaussiano)
fft_ruido_poisson = fft2(ruido_poisson)

#Calculamos transfromada de Fourier en la imagen
fft_imagen = fft2(imagen)

#Centramos el espectro de Fourier en el centro
fft_imagen_cent = fftshift(fft_imagen)

# Calculamos espetro de amplitud del espectro de Fourier centrado
espectro_amp = np.abs(fft_imagen_cent)


plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(np.log(1 + np.abs(fftshift(fft_ruido_gaussiano))))
plt.title('Transformada de Fourier - Ruido Gaussiano')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(np.log(1 + espectro_amp))
plt.title('Espectro de Amplitud')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(np.log(1 + np.abs(fftshift(fft_ruido_poisson))))
plt.title('Transformada de Fourier - Ruido de Poisson')
plt.axis('off')

plt.show()


# ##################################################################


###################Comparacion de distribuciones.########################

# Obtener las intensidades de los píxeles
pixel_intensities = imagen.flatten()

# Definir las distribuciones candidatas
distributions = [stats.norm, stats.rayleigh, stats.gamma]

# Ajustar las distribuciones y calcular la bondad del ajuste (usando la prueba de Kolmogorov-Smirnov)
fit_params = []

for distribution in distributions:
    fit_result = distribution.fit(pixel_intensities)
    # Almacenamos los parámetros del ajuste para mostrarlos más tardes
    fit_params.append(fit_result)  

    # Convertimos el len de los pixeles en un entero
    sample_size = int(len(pixel_intensities))
    

# Graficar de los histogramas de todas las distribuciones ajustadas

for i, distribution in enumerate(distributions):
    fit_data = distribution.rvs(size=sample_size, *fit_params[i])
    plt.hist(pixel_intensities, bins=20, alpha=0.5, label='Datos Originales')
    plt.hist(fit_data, bins=20, alpha=0.5, label=f'{distribution.name}')
    plt.legend()
    plt.title('Ajuste de Distribuciones')
    plt.show()








