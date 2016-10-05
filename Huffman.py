# -*- coding: utf-8 -*-
"""

"""

#from cdi20152016Q1 import *
from collections import Counter
import heapq

class Node(object):
	def __init__(self, pairs, frequency):
		self.pairs = pairs
		self.frequency = frequency

	def __repr__(self):
		return repr(self.pairs) + ", " + repr(self.frequency)

	def __lt__(self, other):
		return self.frequency < other.frequency

	def merge(self, other):
		total_frequency = self.frequency + other.frequency
		for p in self.pairs:
			p[1] = "1" + p[1]
		for p in other.pairs:
			p[1] = "0" + p[1]
		new_pairs = self.pairs + other.pairs
		return Node(new_pairs, total_frequency)


'''
Dada una distribucion de probabilidad, hallar un código de Huffman asociado
'''

'''
def Huffman(p):
	code = [None] * len(p)
	sorted(p)
	while(len(p) > 1):
		for element in p:
			if(element[0] < min1):
				min1 = element[0]
				pos1 = element[1]
			elif(element[0] < min2):
				min2 = element[0]
				pos2 = element[1]
		for e1 in pos1:
			code[e1] += '0'
		for e2 in pos2:
			code[e2] += '1'
	
    return code
'''

def Huffman(p):
	table = [Node([[pos, '']], p[pos]) for pos in range(0,len(p))]
	heapq.heapify(table)
	while len(table) > 1:
		first_node = heapq.heappop(table)
		second_node = heapq.heappop(table)
		new_node = first_node.merge(second_node)
		heapq.heappush(table, new_node)
	return dict(table[0].pairs)
	

def Huffman2(t):
	table = [Node([[ch, '']], freq) for ch,freq in t.items()]
	heapq.heapify(table)
	while len(table) > 1:
		first_node = heapq.heappop(table)
		second_node = heapq.heappop(table)
		new_node = first_node.merge(second_node)
		heapq.heappush(table, new_node)
	return dict(table[0].pairs)

'''
Dada la ddp p=[0.80,0.1,0.05,0.05], hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

p=[0.80,0.1,0.05,0.05]



'''
Dada la ddp p=[1/n,..../1/n] con n=2**8, hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

n=2**8
p=[1/n for _ in range(n)]







'''
Dado un mensaje hallar la tabla de frecuencia de los caracteres que lo componen
'''
def tablaFrecuencias(mensaje):
	total = len(mensaje)
	c = Counter(mensaje)
	return {key:value/total for key,value in c.items()} #iteritems python2


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

'''
Definir una función que codifique un mensaje utilizando un código de Huffman 
obtenido a partir de las frecuencias de los caracteres del mensaje.

Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''

def EncodeHuffman(mensaje_a_codificar):
	m2c = Huffman2(mensaje_a_codificar)	
	mensaje_codificado = ''
	for tmp in mensaje_a_codificar:
		mensaje_codificado += m2c[tmp]
	return mensaje_codificado, m2c


def DecodeHuffman(mensaje_codificado,m2c):
	c2m = {value: key for key, value in m2c.items()}
	return Decode(mensaje_codificado, c2m)


'''
Ejemplo
'''
mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
mensaje_codificado, m2c=EncodeHuffman(mensaje)
mensaje_recuperado=DecodeHuffman(mensaje_codificado,m2c)
print(mensaje_recuperado)
ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
print(ratio_compresion)

