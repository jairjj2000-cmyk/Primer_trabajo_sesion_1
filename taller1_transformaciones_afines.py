import numpy as np

# 1. Crear una matriz de prueba 5x5 con valores sobreexpuestos (entre 200 y 255)
matriz_original = np.random.randint(200, 255, (5, 5))

alpha = 0.5
beta = -50
matriz_transformada = alpha * matriz_original + beta

# 3. Limitar valores al rango válido [0, 255] con np.clip() y convertir a np.uint8
matriz_procesada = np.clip(matriz_transformada, 0, 255).astype(np.uint8)

# 4. Imprimir ambas matrices para comparar
print("=== MATRIZ ORIGINAL (Sobreexpuesta) ===")
print(matriz_original)

print("\n=== MATRIZ PROCESADA (Contraste -50%, Brillo -50) ===")
print(matriz_procesada)
