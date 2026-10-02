def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(b) != len(a[0]):
		return -1
	else:
		c =[]
		for i in range(len(a)):
			y = 0
			for k in range(len(b)):
				x = a[i][k]*b[k]
				y += x
			c.append(y)
	return c
				



