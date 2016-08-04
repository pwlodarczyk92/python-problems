# user starts at coordinates (0, 0).
# by entering 'a', 'w', 's' and 'd' characters, user moves by one unit in given direction.
# after every move, his current coordinates are printed.
# after pressing 'x' character, program quits.
# after pressing 'p', program saves point as next vertex of the polygon.
# after entering 'q', program prints circumference of the polygon and quits.
#
# example:pass direction - d
# current coordinates: (1, 0)
# pass direction - w
# current coordinates: (1, 1)
# pass direction - p
# appending point: (1, 1)
# pass direction - a
# current coordinates: (0, 1)
# pass direction - a
# current coordinates: (-1, 1)
# pass direction - p
# appending point: (-1, 1)
# pass direction - s
# current coordinates: (-1, 0)
# pass direction - d
# current coordinates: (0, 0)
# pass direction - p
# appending point: (0, 0)
# pass direction - q
# circumference = 4.82842712474619


from math import sqrt
moves = 'awsd'
current = (0, 0)
vertices = []
fin = False

while not fin:

	data = input("pass direction - ")

	if data in moves:
		if data == 'a':
			current = (current[0] - 1, current[1])
		if data == 'w':
			current = (current[0], current[1] + 1)
		if data == 's':
			current = (current[0], current[1] - 1)
		if data == 'd':
			current = (current[0] + 1, current[1])
		print("current coordinates: " + str(current))

	elif data == "p":
		print("appending point: " + str(current))
		vertices.append(current)

	elif data == "x":
		fin = True
		print("closing the program.")

	elif data == "q":

		fin = True

		def dist(p1, p2):
			dx = p1[0]-p2[0]
			dy = p1[1]-p2[1]
			return sqrt(dx*dx + dy*dy)

		circumference = dist(vertices[0], vertices[len(vertices)-1])
		for x in range(len(vertices)-1):
			circumference += dist(vertices[x], vertices[x+1])

		print("circumference = " + str(circumference))

	else:
		print("wrong string passed")