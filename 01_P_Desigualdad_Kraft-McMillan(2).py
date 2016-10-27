# -*- coding: utf-8

import math

'''
Dada la lista L de longitudes de las palabras de un código 
r-ario, decidir si pueden definir un código.

'''

def  kraft1(L, r=2):
	maxim = max(L)
		
	tmp1 = r**maxim
	tmp2 = 0
		
	for element in L:
		tmp2 += r**(maxim-element)
		
	if(tmp1 - tmp2 >= 0):
		return True

	return False




'''
Dada la lista L de longitudes de las palabras de un código 
r-ario, calcular el máximo número de palabras de longitud 
máxima, max(L), que se pueden añadir y seguir siendo un código.
'''

def  kraft2(L, r=2):
	maxim = max(L)
		
	tmp1 = r**maxim
	tmp2 = 0
		
	for element in L:
		tmp2 += r**(maxim-element)

	return tmp1-tmp2

'''
Dada la lista L de longitudes de las palabras de un  
código r-ario, calcular el máximo número de palabras 
de longitud Ln, que se pueden añadir y seguir siendo 
un código.
'''

def  kraft3(L, Ln, r=2):
	tmp1 = r**Ln
	tmp2 = 0
		
	for element in L:
		if(element < Ln):
			tmp2 += r**(Ln-element)
		else:
			tmp2 += 1/r**(element-Ln)
	tmp2 = math.ceil(tmp2)

	return tmp1-tmp2


'''
Dada la lista L de longitudes de las palabras de un  
código r-ario, hallar un código prefijo con palabras 
con dichas longiutudes
'''
def Code(L,r=2):
	c = []	
	return c


'''
Ejemplo
'''

L=[1,3,5,5,10,3,5,7,8,9,9,2,2,2]
print(kraft1(L))

L=[2,2,4,4,4,4,5,5,5,5]
print(kraft1(L))
print('Max (5): ',kraft2(L))
print('3: ',kraft3(L, 3))


