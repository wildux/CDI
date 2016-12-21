import numpy as np
from numpy.linalg import inv
import math

_3e3 = math.sqrt(3)/3
_2e2 = math.sqrt(2)/2
_6e3 = math.sqrt(6)/3
_6e6 = math.sqrt(6)/6


mat = [[_3e3, _3e3, _3e3], [-_2e2, _2e2, 0.], [-_6e6, -_6e6, _6e3]]
#mat = [[1., 1., 1.], [2., 2., 2.], [-1., -1., 2.]]
#mat = [[1., 1., 1.], [-1., -1., 0.], [-1., -1., 2.]]
#mat = [[_3e3, _3e3, _3e3], [_2e2, _2e2, _2e2], [-_6e6, -_6e6, _6e3]]

import numpy

try:
	result = np.matrix(list(map(list, zip(*mat))))
	result2 = inv(mat)
	print(result)
	print(result2)
	if np.allclose(result, result2):
		print("SON ORTOGONALS")
	else:
		print("CACA")
except numpy.linalg.linalg.LinAlgError as err:
	if 'Singular matrix' in str(err):
		print("MATRIU SINGULAR")
	else:
		raise








