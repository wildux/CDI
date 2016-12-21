# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import scipy
import scipy.ndimage
import time
from scipy.fftpack import dct, idct
import math 
pi=math.pi

import matplotlib.pyplot as plt


"""
Matrices de cuantización, estándares y otras
"""

Q_Luminance=np.array([
	[16 ,11, 10, 16,  24,  40,  51,  61],
	[12, 12, 14, 19,  26,  58,  60,  55],
	[14, 13, 16, 24,  40,  57,  69,  56],
	[14, 17, 22, 29,  51,  87,  80,  62],
	[18, 22, 37, 56,  68, 109, 103,  77],
	[24, 35, 55, 64,  81, 104, 113,  92],
	[49, 64, 78, 87, 103, 121, 120, 101],
	[72, 92, 95, 98, 112, 100, 103,  99]])


Q_Chrominance=np.array([
	[17, 18, 24, 47, 99, 99, 99, 99],
	[18, 21, 26, 66, 99, 99, 99, 99],
	[24, 26, 56, 99, 99, 99, 99, 99],
	[47, 66, 99, 99, 99, 99, 99, 99],
	[99, 99, 99, 99, 99, 99, 99, 99],
	[99, 99, 99, 99, 99, 99, 99, 99],
	[99, 99, 99, 99, 99, 99, 99, 99],
	[99, 99, 99, 99, 99, 99, 99, 99]])

def Q_matrix(r=1):
	m=np.zeros((8,8))
	for i in range(8):
		for j in range(8):
			m[i,j]=(1+i+j)*r
	return m

"""
Implementar la DCT (Discrete Cosine Transform) 
y su inversa para bloques NxN

dct_bloque(p,N)
idct_bloque(p,N)

p bloque NxN

"""

def dct_bloque(p):
	return scipy.fftpack.dct(scipy.fftpack.dct(np.array(p, dtype=float),axis=0),axis=1)

def idct_bloque(p):
	return scipy.fftpack.idct(scipy.fftpack.idct(np.array(p, dtype=float),axis=0),axis=1)


"""
Reproducir los bloques base de la transformación para los casos N=4,8
Ver imágenes adjuntas.
"""

def repr_bloques(N=4):
	fig = plt.figure()
	for i in range(N):
		for j in range(N):
			m = np.zeros((N,N))
			m[i,j]= 1
			imgI = idct_bloque(m)
			fig.add_subplot(N,N,(i*N)+j+1),plt.imshow(imgI)
			plt.xticks([]),plt.yticks([])
	fig.show()

repr_bloques()


"""
Implementar la función jpeg_gris(imagen_gray) que: 
1. dibuje el resultado de aplicar la DCT y la cuantización 
(y sus inversas) a la imagen de grises 'imagen_gray' 

2. haga una estimación de la ratio de compresión
según los coeficientes nulos de la transformación: 
(#coeficientes/#coeficientes no nulos).

3. haga una estimación del error
Sigma=np.sqrt(sum(sum((imagen_gray-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_gray)**2)))


En este caso optimizar la DCT 
http://docs.scipy.org/doc/numpy-1.10.1/reference/routines.linalg.html
"""


def jpeg_gris(imagen_gray):
	N = 8
	n, m = imagen_gray.shape
	imagen_gray = imagen_gray - 128
	for i in range(0,m,N):
		for j in range(0,n,N):
			dct = dct_bloque(imagen_gray[i:i+N,j:j+N]) / Q_Luminance
			imagen_gray[i:i+N,j:j+N] = idct_bloque(dct)
	return imagen_gray

"""
Implementar la función jpeg_color(imagen_color) que: 
1. dibuje el resultado de aplicar la DCT y la cuantización 
(y sus inversas) a la imagen RGB 'imagen_color' 

2. haga una estimación de la ratio de compresión
según los coeficientes nulos de la transformación: 
(#coeficientes/#coeficientes no nulos).

3. haga una estimación del error para cada una de las componentes RGB
Sigma=np.sqrt(sum(sum((imagen_color-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_color)**2)))


En este caso optimizar la DCT 
http://docs.scipy.org/doc/numpy-1.10.1/reference/routines.linalg.html
"""



def jpeg_color(imagen_color):
	N = 8
	n, m, d = imagen_color.shape
	imagen_color = imagen_color - 128
	for i in range(0,m,N):
		for j in range(0,n,N):
			for c in range(d):
				dct = dct_bloque(imagen_color[i:i+N,j:j+N,c]) / Q_Chrominance
				imagen_color[i:i+N,j:j+N,c] = idct_bloque(dct)
			#dct = dct_bloque(imagen_color[i:i+N,j:j+N,1]) / Q_Chrominance
			#imagen_color[i:i+N,j:j+N,1] = idct_bloque(dct)
			#dct = dct_bloque(imagen_color[i:i+N,j:j+N,2]) / Q_Chrominance
			#imagen_color[i:i+N,j:j+N,2] = idct_bloque(dct)
	return imagen_color

"""
#--------------------------------------------------------------------------
Imagen de GRISES

#--------------------------------------------------------------------------
"""


### .astype es para que lo lea como enteros de 32 bits, si no se
### pone lo lee como entero positivo sin signo de 8 bits uint8 y por ejemplo al 
### restar 128 puede devolver un valor positivo mayor que 128

mandril_gray=scipy.ndimage.imread('mandril_gray.png').astype(np.int32)
fig = plt.figure()
fig.add_subplot(1,2,1),plt.imshow(mandril_gray,'gray')
plt.xticks([]),plt.yticks([])

start= time.clock()
mandril_jpeg=jpeg_gris(mandril_gray)
end= time.clock()
print("tiempo Gris",(end-start))

#SHOW
fig.add_subplot(1,2,2),plt.imshow(mandril_jpeg,'gray')
plt.xticks([]),plt.yticks([])
fig.show()

#COMPRESSIÓ


#ERROR
Sigma = np.sqrt(sum(sum((mandril_gray-mandril_jpeg)**2)))/np.sqrt(sum(sum((mandril_gray)**2)))
print("Sigma Gris",Sigma)


"""
#--------------------------------------------------------------------------
Imagen COLOR
#--------------------------------------------------------------------------
"""
## Aplico.astype pero después lo convertiré a 
## uint8 para dibujar y a int64 para calcular el error

mandril_color=scipy.misc.imread('./mandril_color.png').astype(np.int32)
fig = plt.figure()
fig.add_subplot(1,2,1),plt.imshow(mandril_color.astype(np.uint8))
plt.xticks([]),plt.yticks([])

start= time.clock()
mandril_jpeg=jpeg_color(mandril_color)     
end= time.clock()
print("tiempo Color",(end-start))

#SHOW
#image = (mandril_jpeg * 255).round().astype(np.uint8)
fig.add_subplot(1,2,2),plt.imshow(mandril_jpeg.astype(np.uint8))
#fig.add_subplot(1,2,2),plt.imshow(image)
plt.xticks([]),plt.yticks([])
fig.show()

#COMPRESSIÓ


#ERROR
#Sigma = np.sqrt(sum(sum((mandril_color-mandril_jpeg)**2)))/np.sqrt(sum(sum((mandril_color)**2)))
#print("Sigma",Sigma)


while True:
	input("Enter text (or Enter to quit): ")
	break
