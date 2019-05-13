import numpy

v1 = numpy.array([1.0, 1.0, 1.0, 0.0, 1.0], dtype=float)
v2 = numpy.array([1.0, 0.0, 1.0, 1.0, 1.0], dtype=float)

print(numpy.dot(v1, v2) / (numpy.linalg.norm(v1) * numpy.linalg.norm(v2)))
