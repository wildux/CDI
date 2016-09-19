# -*- coding: utf-8 -*-

import random

'''
0. Dada una codificación R, construir un diccionario para codificar m2c y otro para decodificar c2m
'''

R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])


'''
1. Definir una función Encode(M, m2c) que, dado un mensaje M y un diccionario 
de codificación m2c, devuelva el mensaje codificado C.
'''

def Encode(M, m2c):
	C = ''
	for tmp in M:
		C += m2c[tmp]
	return C


'''
2. Definir una función Decode(C, m2c) que, dado un mensaje codificado C y un diccionario 
de decodificación c2m, devuelva el mensaje original M.
'''

def Decode(C,c2m):
	M = ''
	tmp2 = ''
	l = len(C)
	x = 1
	reverse = False
	for tmp in C:
		tmp2 += tmp
		if(tmp2 in c2m):
			M += c2m[tmp2]
			tmp2 = ''
		elif(x == l):
			reverse = True
		x+=1
	
	if(reverse):
		M = ''
		tmp2 = ''
		C2 = C[::-1]
		for tmp in C2:
			tmp2 = tmp + tmp2
			if(tmp2 in c2m):
				M = c2m[tmp2] + M
				tmp2 = ''

	return M


#------------------------------------------------------------------------
# Ejemplo 1
#------------------------------------------------------------------------

R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

'''
3. Generar un mensaje aleatorio M de longitud 50 con las frecuencias 
esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.
'''

def Generate(s):
	msg = ''
	for x in range(0, s):
		r = random.randint(1,100)
		if(r < 51):
			 msg += 'a'
		elif(r < 71):
			 msg += 'b'
		elif(r < 86):
			 msg += 'c'
		elif(r < 96):
			 msg += 'd'
		else:
			 msg += 'e'
	return msg


msg = Generate(50)
encoded = Encode(msg, m2c)

''' 
4. Si 'a', 'b', 'c', 'd', 'e' se codifican inicialmente con un código de 
bloque de 3 bits, hallar la ratio de compresión al utilizar el nuevo código.  
'''

r = (3*50) / (25 + 10*2 + 7.5*3 + 5*4 + 2.5*4)
r2 = 3*50 / len(encoded)

print('R teòric: ',r)
print('R msg generat: ',r2)


#------------------------------------------------------------------------
# Ejemplo 2
#------------------------------------------------------------------------
R = [('a','0'), ('b','10'), ('c','110'), ('d','1110'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
5.
Codificar y decodificar 20 mensajes aleatorios de longitudes también aleatorios.  
Comprobar si los mensajes decodificados coinciden con los originales.
'''

for x in range(0, 20):
	s = random.randint(1,10000)
	msg = Generate(s)
	encoded = Encode(msg, m2c)
	decoded = Decode(encoded, c2m)
	if(decoded != msg):
		 print("Error", x)


#------------------------------------------------------------------------
# Ejemplo 3 
#------------------------------------------------------------------------
R = [('a','0'), ('b','01'), ('c','011'), ('d','0111'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
6. Codificar y decodificar los mensajes  'ae' y 'be'. 
Comprobar si los mensajes decodificados coinciden con los originales.
'''

encoded = Encode('ae', m2c)
print(Decode(encoded, c2m) )

encoded2 = Encode('be', m2c)
print(Decode(encoded2, c2m) )

#Proves

for x in range(0, 30):
	s = random.randint(1,10000)
	msg = Generate(s)
	encoded = Encode(msg, m2c)
	decoded = Decode(encoded, c2m)
	if(decoded != msg):
		 print("Error", x)
