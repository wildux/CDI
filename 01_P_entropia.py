# -*- coding: utf-8 -*-
"""
Joan Rodas Cusidó
"""
import math
import numpy as np
import matplotlib.pyplot as plt

'''
Dada una lista p, decidir si es una distribución de probabilidad (ddp)
0<=p[i]<=1, sum(p[i])=1.
'''

def es_ddp(p,tolerancia=10**(-5)):
	suma = 0
	for element in p:
		if element < 0:
			return false
		suma += element
	if (suma >= 1 - tolerancia) and (suma <= 1 + tolerancia):
		return True
	return False

'''
Dado un código C y una ddp p, hallar la longitud media del código.
'''

def LongitudMedia(C,p):
	l = 0
	i = 0
	for element in C:
		l += ( len(element)*p[i] )
		i += 1
	return l

'''
Dada una ddp p, hallar su entropía.
'''

def H1(p):
	e = 0
	for element in p:
		if element > 10**(-5):
			e += element * math.log(element, 2)
	return -e


'''
Dada una lista de frecuencias n, hallar su entropía.
'''

def H2(n):
	suma = 0
	e = 0
	for element in n:
		suma += element
	for element in n:
		if element > 10**(-5):
			element = element/suma
			e += element * math.log(element, 2)
	return -e


'''
Ejemplos
'''

C=['001','101','11','0001','000000001','0001','0000000000']
p=[0.5,0.1,0.1,0.1,0.1,0.1,0]
n=[5,2,1,1,1]


print('És ddp? ',es_ddp(p))
print('H1: ',H1(p))
print('H2: ',H2(n))
print('Long: ',LongitudMedia(C,p))


'''
Dibujar H(p,1-p)
'''
def draw():
	x = []
	y = []
	for p in np.arange(0, 1.01, 0.01):
		x.append(p)
		y.append(H1([p,1-p]))
	plt.plot(x, y)
	plt.show()


'''
Hallar aproximadamente el máximo de  H(p,q,1-p-q)
'''

def find_max():
	maxim = 0
	for p in np.arange(0, 1.01, 0.01):
		for q in np.arange(0, 1.01, 0.01):
			if p + q <= 1 and H1([p,q,1-p-q]) > maxim:
				maxim = H1([p,q,1-p-q])
	return maxim


draw()
print('Màxim: ',find_max())
