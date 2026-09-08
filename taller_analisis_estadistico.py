import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar imagen
imagen = cv2.imread("imagen.jpg")

# 2. Separar en canales B, G, R
b, g, r = cv2.split(imagen)

# 3. Calcular promedios de intensidad
media_b = np.mean(b)
media_g = np.mean(g)
media_r = np.mean(r)

print("--- Intensidad promedio por canal ---")
print(f"Azul  (B): {media_b:.2f}")
print(f"Verde (G): {media_g:.2f}")
print(f"Rojo  (R): {media_r:.2f}")

if media_b > media_g and media_b > media_r:
    print("\nColor dominante en la iluminacion general: AZUL")
elif media_g > media_b and media_g > media_r:
    print("\nColor dominante en la iluminacion general: VERDE")
else:
    print("\nColor dominante en la iluminacion general: ROJO")

# 4. Calcular histograma de cada canal
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# 5. Graficar los histogramas superpuestos
plt.figure(figsize=(8, 5))
plt.plot(hist_b, color='b', label='Azul (B)')
plt.plot(hist_g, color='g', label='Verde (G)')
plt.plot(hist_r, color='r', label='Rojo (R)')

plt.title("Histograma de canales RGB")
plt.xlabel("Intensidad (0 - 255)")
plt.ylabel("Pixeles")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Guardar la figura
plt.savefig("grafica_canales.png")
