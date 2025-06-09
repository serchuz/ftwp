# %%
c = (-9.5, 11.75)
type(c)
# <class 'tuple'>
# %%
c
# %%
c[0]


# %%
i = 0.1
def D(c1):
    return c1 / (1 + i)

# %%
D(100)
# %%
import numpy as np
# %%
a = np.array([1, 2, 3])
# %%
type(a)
# %%
a * 2 + 5
# %%

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 * arr2) # Salida: [ 4 10 18] (1*4, 2*5, 3*6)

matriz1 = np.array([[1, 2],
                    [3, 4]])
matriz2 = np.array([[5, 6],
                    [7, 8]])
print(matriz1 * matriz2)
# %%
matriz1 @ matriz2
# %%
import numpy as np
import matplotlib.pyplot as plt

# Crear un generador de números aleatorios
rng = np.random.default_rng(42) # Seeding para reproducibilidad

# Generar 10000 números aleatorios con rng.random()
uniform_samples = rng.random(10000)

# Generar 10000 números aleatorios con rng.standard_normal()
normal_samples = rng.standard_normal(10000)

# Graficar las distribuciones para visualizarlas
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(uniform_samples, bins=30, density=True, alpha=0.7, color='skyblue')
plt.title('Distribución Uniforme (rng.random())')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.hist(normal_samples, bins=30, density=True, alpha=0.7, color='lightcoral')
plt.title('Distribución Normal Estándar (rng.standard_normal())')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.grid(True)

plt.tight_layout()
plt.show()
# %%
