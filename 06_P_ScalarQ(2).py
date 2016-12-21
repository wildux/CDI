# -*- coding: utf-8 -*-

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

"""
Joan Rodas
"""
#np.set_printoptions(threshold=np.inf)

imagen = misc.ascent()	#Leo la imagen
(n,m)=imagen.shape		#filas y columnas de la imagen

"""
Mostrar la imagen habiendo cuantizado los valores de los píxeles en
2**k niveles, k=1..8

Para cada cuantización dar la ratio de compresión y Sigma

Sigma=np.sqrt(sum(sum((imagenOriginal-imagenCuantizada)**2)))/(n*m)
"""


def quant(img,k):
	n = 2**(8-k)
	return img//n*n


img = quant(imagen,2)
Sigma = np.sqrt(sum(sum((imagen-img)**2)))/(n*m)

plt.imshow(img, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()


"""
Mostrar la imagen cuantizando los valores de los pixeles de cada bloque
n_bloque x n_bloque en 2^k niveles, siendo n_bloque=8 y k=2

Calcular Sigma y la ratio de compresión (para cada bloque 
es necesario guardar 16 bits extra para los valores máximos 
y mínimos del bloque, esto supone 16/n_bloque**2 bits más por pixel).
"""

def quant_bloc(img,k=2,n_bloque=8):
	for x in range(0,m,n_bloque):
		for y in range(0,n,n_bloque):
			maxim = np.amax(img[x:x+n_bloque, y:y+n_bloque])
			minim = np.amin(img[x:x+n_bloque, y:y+n_bloque])
			img[x:x+n_bloque, y:y+n_bloque] = ((img[x:x+n_bloque, y:y+n_bloque] - minim) * 2**k ) // (maxim)
	return img

img = quant_bloc(imagen,8,128)

plt.imshow(img, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()

#Sigma2 = np.sqrt(sum(sum((imagen-img)**2)))/(n*m)
