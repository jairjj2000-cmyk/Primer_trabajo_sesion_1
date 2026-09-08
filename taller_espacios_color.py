import cv2
import numpy as np
import urllib.request

# 1. Pixel amarillo intenso en BGR (Blue=0, Green=255, Red=255)
pixel = np.array([0, 255, 255])
print("Pixel BGR:", pixel)

# 2. Calculo matematico con formula ponderada (0.114*B + 0.587*G + 0.299*R)
b = pixel[0]
g = pixel[1]
r = pixel[2]
gris = 0.114 * b + 0.587 * g + 0.299 * r

# 3. Resultado
print(f"Valor en grises (decimal): {gris:.2f}")
print(f"Valor en grises (0-255): {round(gris)}")

# 4. Conversion con OpenCV usando una imagen
# Descarga de imagen de internet
url = "https://picsum.photos/400/300"
urllib.request.urlretrieve(url, "imagen.jpg")

# Cargar imagen y convertir a escala de grises
imagen = cv2.imread("imagen.jpg")
img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Guardar imagen resultante
cv2.imwrite("imagen_gris.jpg", img_gris)
print("Imagen procesada y guardada como imagen_gris.jpg")
