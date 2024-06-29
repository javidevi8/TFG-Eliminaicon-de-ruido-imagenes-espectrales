# TFG - Eliminación de Ruido en Imágenes Espectrales

Este repositorio contiene el código del Trabajo de Fin de Grado (TFG) que compara el desempeño de dos modelos de aprendizaje automático para la eliminación de ruido en imágenes espectrales: Noise2Void y DnCNN.

## Descripción

El proyecto se centra en la eliminación de ruido en imágenes espectrales obtenidas por ALBA , acelerador de particulas de Barcelona, mediante la técnica de espectrocopia ARPES. El análisis se hace desde dos enfoques diferentes de aprendizaje automático. Noise2Void es un método que no requiere imágenes limpias para el entrenamiento, mientras que DnCNN es un modelo basado en redes neuronales convolucionales entrenado con pares de imágenes ruidosas y limpias.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Modelos](#modelos)
- [Créditos](#créditos)

## Instalación

### Requisitos Previos

- Python 3.8+
- n2v
- [TensorFlow](https://www.tensorflow.org/install) 2.0+ ⚠️ N2v no compatible con Tensoflow 2.16 ⚠️
- [NumPy](https://numpy.org/install/)
- [Matplotlib](https://matplotlib.org/stable/users/installing.html)

Se encuentran en más detalle en el Requirements.txt

### Instrucciones

1. Clona el repositorio:
   ```sh
   git clone https://github.com/javidevi8/TFG-Eliminaicon-de-ruido-imagenes-espectrales.git


## USO
1. Creamos carpeta de Datos con las imagenes espectrales, dentro del directorio en el que se encuentre el modelo que queremos utilizar.
2. Ajustar el modelo a los datos que se tiene.
3. En caso de ser N2V usar archivo de prediction_Noise2Void para comprobar resultados

## Modelos
### Noise2Void
Noise2Void es un enfoque que permite entrenar modelos de denoising sin la necesidad de imágenes limpias como referencia. Utiliza una estrategia de máscara para predecir los valores de los píxeles basándose en el contexto de sus alrededores. En el repositorio encontramos los archivos con los que entrenamos y predecimos, a su vez de una carpeta con el código con las funciones de las que se hace uso en los archivos de entrenamiento y predicción. Para poder utilizar el tensorboard hay que hacer las modificaciones que se encuentran en el archivo n2v_standard.py apartir de la línea 253

Paper: https://arxiv.org/abs/1811.10980

### DnCNN
DnCNN (Denoising Convolutional Neural Network) es una red neuronal convolucional diseñada específicamente para la eliminación de ruido en imágenes. Requiere un conjunto de datos de entrenamiento con imágenes limpias y sus correspondientes versiones ruidosas.
Paper: https://arxiv.org/abs/1608.03981

## Credenciales
Modelo del Noise2Void basado en la interpretacion del paper y de la implementacion del siguiente github: https://github.com/juglab/n2v
