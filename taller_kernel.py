import numpy as np

# Punto 1: Crear las matrices I (Imagen) y K (Kernel)
I = np.array([
    [100, 100, 100],
    [100, 200, 100],
    [100, 100, 100]
])

K = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

print("Matriz Imagen (I):")
print(I)

print("\nMatriz Kernel (K):")
print(K)

# Punto 2: Multiplicacion Hadamard (elemento a elemento)
hadamard = I * K

print("\nProducto Hadamard (I * K):")
print(hadamard)

# Punto 3: Sumar todos los valores de la matriz resultante
pixel_central = np.sum(hadamard)

print(f"\nValor del pixel central calculado: {pixel_central}")
