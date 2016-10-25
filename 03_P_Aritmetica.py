# -*- coding: utf-8 -*-

"""
Joan Rodas Cusidó
"""

import math
import random

"""
Dado x en [0,1) dar su representacion en binario, por ejemplo
dec2bin(0.625)='101'
dec2bin(0.0625)='0001'

Dada la representación binaria de un real perteneciente al intervalo [0,1) 
dar su representación en decimal, por ejemplo

bin2dec('101')=0.625
bin2dec('0001')=0.0625

nb número máximo de bits

"""



def dec2bin(x,nb=100,error=10**-5):
	ant = 0
	tmp = 0
	res = ''
	for b in range(1,nb+1):
		tmp += 2**(-b)
		if tmp > x + error:
			tmp = ant
			res += '0'
		else:
			ant = tmp
			res += '1'
			if not tmp < x - error:
				break
	return res

def dec2bin_i(l,u,nb=100,error=10**-5):
	ant = 0
	tmp = 0
	res = ''
	for b in range(1,nb+1):
		tmp += 2**(-b)
		if tmp > u + error:
			tmp = ant
			res += '0'
		else:
			ant = tmp
			res += '1'
			if not tmp < l - error:
				break
	return res

print('\nDEC2BIN\n--------------------')
print('0.625 -->',dec2bin(0.625))
print('0.0625 -->',dec2bin(0.0625))
print('0.876-0.8776 -->',dec2bin_i(0.876,0.8776))


def bin2dec(xb):
	dec = 0.0
	for x in range(len(xb)):
		if xb[x] == '1':
			dec += 2**-(x+1)
	return dec

print('\nBIN2DEC\n--------------------')
print('101 -->',bin2dec('101'))
print('0001 -->',bin2dec('0001'))
print('111000001-->',bin2dec('111000001'))

"""
Dada una distribución de probabilidad p(i), i=1..n,
hallar su función distribución:
f(0)=0
f(i)=sum(p(k),k=1..i).
"""

def cdf(p):
	res = [0]
	for x in range(len(p)-1):
		res.append(res[x]+p[x])
	return res

print('\nCDF\n--------------------')
p = [0.5,0.2,0.15,0.1,0.05]
print(p,'-->',cdf(p))

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar el intervalo (l,u) que representa al mensaje.

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
Arithmetic(mensaje,alfabeto,probabilidades)=0.876 0.8776
"""

def Arithmetic(mensaje,alfabeto,probabilidades):
	dict_p = {k: v for k, v in zip(alfabeto, probabilidades)}
	dict_ck = {k: v for k, v in zip(alfabeto, cdf(probabilidades))}
	probs = 1
	l = 0
	for x in mensaje:
		tmp = dict_ck[x] * probs
		probs *= dict_p[x]
		l += tmp
	return l, l+probs

print('\nARITHMETIC\n--------------------')
mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
print(mensaje,probabilidades,'-->',Arithmetic(mensaje,alfabeto,probabilidades))

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar la representación binaria de x=r/2**(t) siendo t el menor 
entero tal que 1/2**(t)<l-u, r entero (si es posible par) tal 
que l*2**(t)<=r<u*2**(t)

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
EncodeArithmetic1(mensaje,alfabeto,probabilidades)='111000001'
"""

def EncodeArithmetic1(mensaje,alfabeto,probabilidades):
	t = 1
	l, u = Arithmetic(mensaje,alfabeto,probabilidades)
	tmp = u-l
	for x in range(1,100):
		if (2**x)*tmp > 1:
			t = x
			break
	x = 2**t
	minim = math.ceil(l*x)
	maxim = math.floor(u*x)
	r = minim #BUSCAR PARELL ENTRE MIN I MAX
	return dec2bin(r/(2**t))

print('\nENCODE 1\n--------------------')
mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
print(mensaje,probabilidades,'-->',EncodeArithmetic1(mensaje,alfabeto,probabilidades)) #'111000001'

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar el código que representa el mensaje obtenido a partir de la 
representación binaria de l y u

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
EncodeArithmetic2(mensaje,alfabeto,probabilidades)='111000001'

"""

def EncodeArithmetic2(mensaje,alfabeto,probabilidades):
	l, u = Arithmetic(mensaje,alfabeto,probabilidades)
	return dec2bin_i(l,u)

print('\nENCODE 2\n--------------------')
mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
print(mensaje,probabilidades,'-->',EncodeArithmetic2(mensaje,alfabeto,probabilidades)) #'111000001'

"""
Dada la representación binaria del número que representa un mensaje, la
longitud del mensaje y el alfabeto con su distribución de probabilidad 
dar el mensaje original

code='0'
longitud=4
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
DecodeArithmetic(code,longitud,alfabeto,probabilidades)='aaaa'

code='111000001'
DecodeArithmetic(code,4,alfabeto,probabilidades)='ccda'
DecodeArithmetic(code,5,alfabeto,probabilidades)='ccdab'

"""

def DecodeArithmetic(code,n,alfabeto,probabilidades):
	decoded = ''
	ck = cdf(probabilidades) + [1]
	value = bin2dec(code)
	for i in range(n):
		for x in range(len(probabilidades)):
			if value >= ck[x] and value < ck[x+1]:
				minim = ck[x]
				maxim = ck[x+1]
				value = (value-minim)/(maxim-minim)
				decoded += alfabeto[x]
				break
	return decoded

print('\nDECODE\n--------------------')
code='111000001'
print(code,'4',DecodeArithmetic(code,4,alfabeto,probabilidades))
print(code,'5',DecodeArithmetic(code,5,alfabeto,probabilidades))
print('0','4',DecodeArithmetic('0',4,alfabeto,probabilidades))

print('\n\n')

'''
Función que compara la longitud esperada del 
mensaje con la obtenida con la codificación aritmética
'''

def comparacion(mensaje,alfabeto,probabilidades):
	p=1.
	indice=dict([(alfabeto[i],i+1) for i in range(len(alfabeto))])
	for i in range(len(mensaje)):
		p=p*probabilidades[indice[mensaje[i]]-1]
	aux=-math.log(p,2), len(EncodeArithmetic1(mensaje,alfabeto,probabilidades)), len(EncodeArithmetic2(mensaje,alfabeto,probabilidades))
	print('Información y longitudes:',aux)    
	return aux

'''
Generar 10 mensajes aleatorios M de longitud 10<=n<=20 aleatoria 
con las frecuencias esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e', codificarlo y compararlas longitudes 
esperadas con las obtenidas.
'''

alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]
U = 50*'a'+20*'b'+15*'c'+10*'d'+5*'e'
def rd_choice(X,k = 1):
	Y = []
	for _ in range(k):
		Y +=[random.choice(X)]
	return Y

l_max=20

for _ in range(10):
	n=random.randint(10,l_max)
	L = rd_choice(U, n)
	mensaje = ''
	for x in L:
		mensaje += x
	print('----------\n'+mensaje)    
	C=comparacion(mensaje,alfabeto,probabilidades)
	#print(C)

print('\n\n')

'''
Generar 10 mensajes aleatorios M de longitud 10<=n<=100 aleatoria 
con las frecuencias esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.
'''
alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]
U = 50*'a'+20*'b'+15*'c'+10*'d'+5*'e'
def rd_choice(X,k = 1):
	Y = []
	for _ in range(k):
		Y +=[random.choice(X)]
	return Y

l_max=100

for _ in range(10):
	n=random.randint(10,l_max)
	L = rd_choice(U, n)
	mensaje = ''
	for x in L:
		mensaje += x
	print('----------\n'+mensaje)    
	C = EncodeArithmetic1(mensaje,alfabeto,probabilidades)
	print(C)

print('\nPROVES---------------\n')
mensaje = 'aaaaaabbbaecdbabcaa'
alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]

res1 = EncodeArithmetic1(mensaje,alfabeto,probabilidades)
print(mensaje,probabilidades,'-->',res1)
res2 = EncodeArithmetic2(mensaje,alfabeto,probabilidades)
print(mensaje,probabilidades,'-->',res2)

print(res1,'19',DecodeArithmetic(res1,19,alfabeto,probabilidades))
print(res2,'19',DecodeArithmetic(res1,19,alfabeto,probabilidades))

mensaje = 'acadcbaaaccaaaaaacd'

print('\n')
res1 = EncodeArithmetic1(mensaje,alfabeto,probabilidades)
print(mensaje,probabilidades,'-->',res1)
res2 = EncodeArithmetic2(mensaje,alfabeto,probabilidades)
print(mensaje,probabilidades,'-->',res2)

print(res1,'19',DecodeArithmetic(res1,19,alfabeto,probabilidades))
print(res2,'19',DecodeArithmetic(res1,19,alfabeto,probabilidades))


print('\n\n\n')
dict_p = {k: v for k, v in zip(alfabeto, probabilidades)}
dict_ck = {k: v for k, v in zip(alfabeto, cdf(probabilidades))}

print(dict_p)
print(dict_ck)
