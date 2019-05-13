import numpy

v = numpy.array([2.0, 4.0, 6.0], dtype=float)

norm = numpy.linalg.norm(v, ord=2)
v = v / norm

print(norm)
print(v)