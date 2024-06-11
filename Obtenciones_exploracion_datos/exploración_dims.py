from PIL import Image

def obtener_dimensiones_imagen(ruta_imagen):
    imagen = Image.open(ruta_imagen)
    dimensiones = imagen.size  
    canales = imagen.mode
    return dimensiones, canales

ruta_imagen = "C:/Users/JDevi/OneDrive/Escritorio/4_INSO/TFG/Programas/Datos/dimension0_000.png" 
dimensiones,canales = obtener_dimensiones_imagen(ruta_imagen)
print("Dimensiones de la imagen:", dimensiones) 
print("Canales de color:", canales)