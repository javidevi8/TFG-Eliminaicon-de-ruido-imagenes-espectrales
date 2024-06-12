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
- [TensorFlow](https://www.tensorflow.org/install) 2.0+ ⚠️ N2v no compatible con Tensoflow 2.16 ⚠️
- [NumPy](https://numpy.org/install/)
- [Matplotlib](https://matplotlib.org/stable/users/installing.html)

### Instrucciones

1. Clona el repositorio:
   ```sh
   git clone https://github.com/javidevi8/TFG-Eliminaicon-de-ruido-imagenes-espectrales.git

## Modelos
### Noise2Void
Noise2Void es un enfoque que permite entrenar modelos de denoising sin la necesidad de imágenes limpias como referencia. Utiliza una estrategia de máscara para predecir los valores de los píxeles basándose en el contexto de sus alrededores.
Paper: https://arxiv.org/abs/1811.10980

### DnCNN
DnCNN (Denoising Convolutional Neural Network) es una red neuronal convolucional diseñada específicamente para la eliminación de ruido en imágenes. Requiere un conjunto de datos de entrenamiento con imágenes limpias y sus correspondientes versiones ruidosas.
