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
