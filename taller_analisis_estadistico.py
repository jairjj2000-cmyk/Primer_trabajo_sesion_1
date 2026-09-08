import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar la imagen
imagen = cv2.imread("imagen.jpg")

# 2. Separar en canales B, G, R
b, g, r = cv2.split(imagen)

# 3. Calcular histograma de cada canal
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# 4. Graficar los canales superpuestos
plt.figure(figsize=(8, 5))
plt.plot(hist_b, color='b', label='Azul (B)')
plt.plot(hist_g, color='g', label='Verde (G)')
plt.plot(hist_r, color='r', label='Rojo (R)')

plt.title("Analisis de canales de color")
plt.xlabel("Intensidad (0 - 255)")
plt.ylabel("Numero de pixeles")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 5. Analisis del color dominante
media_b = np.mean(b)
media_g = np.mean(g)
media_r = np.mean(r)

print(f"Promedios de intensidad -> Azul: {media_b:.2f}, Verde: {media_g:.2f}, Rojo: {media_r:.2f}")

if media_g > media_r and media_g > media_b:
    print("Conclusion: El color dominante en la iluminacion general es el VERDE.")
elif media_r > media_g and media_r > media_b:
    print("Conclusion: El color dominante en la iluminacion general es el ROJO.")
else:
    print("Conclusion: El color dominante en la iluminacion general es el AZUL.")
