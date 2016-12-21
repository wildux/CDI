# -*- coding: utf-8 -*-


########################################################

import numpy as np
import matplotlib.pyplot as plt

"""
Implementar la DWHT Discrete Walsh-Hadamard Transform y su inversa
para bloques NxN 

dwht_bloque(p,HWH,N) 
idwht_bloque(p,HWH,N) 

p bloque NxN
HWH matriz de la transformación
"""

def WHT(x):
	# Function computes (slow) Discrete Walsh-Hadamard Transform
	# for any 1D real-valued signal
	# (c) 2015 QuantAtRisk.com, by Pawel Lachowicz
	x=np.array(x)
	if(len(x.shape)<2): # make sure x is 1D array
		if(len(x)>3):   # accept x of min length of 4 elements (M=2)
			# check length of signal, adjust to 2**m
			n=len(x)
			M=trunc(log(n,2))
			x=x[0:2**M]
			h2=np.array([[1,1],[1,-1]])
			for i in xrange(M-1):
				if(i==0):
					H=np.kron(h2,h2)
				else:
					H=np.kron(H,h2)
			return (np.dot(H,x)/2.**M, x, M)
		else:
			print("HWT(x): Array too short!")
			raise SystemExit
	else:
		print("HWT(x): 1D array expected!")
		raise SystemExit


def dwht_bloque(p,HWH=HWH8,n_bloque=8):
	return scipy.fftpack.dct(scipy.fftpack.dct(np.array(p, dtype=float),axis=0),axis=1)

def idwht_bloque(p,HWH=HWH8,n_bloque=8):
	return scipy.fftpack.idct(scipy.fftpack.idct(np.array(p, dtype=float),axis=0),axis=1)

"""
Reproducir los bloques base de la transformación para los casos N=4,8 (Ver imágenes adjuntas)
"""

def repr_bloques(N=4):
	fig = plt.figure()
	for i in range(N):
		for j in range(N):
			m = np.zeros((N,N))
			m[i,j]= 1
			imgI = idct(m)
			fig.add_subplot(N,N,(i*N)+j+1),plt.imshow(imgI)
			plt.title("a")
			plt.xticks([]),plt.yticks([])
	fig.show()
	
repr_bloques()
while True:
	input("Enter text (or Enter to quit): ")
