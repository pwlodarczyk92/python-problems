# write program that reads two integers - pair of user's coordinates on a map (x and y).
# by entering 'a', 'w', 's' and 'd' characters, user moves by one unit in given direction.
# after every move, his current coordinates are printed.
# after reaching home, victory message is printed.
# after pressing 'x' character, program quits.
# after entering any other string, program prints about error message and waits for another try.
#
# example:pass user x coordinate - 1
# pass user y coordinate - 0
# pass direction - s
# user's coordinates: (1,-1)
# pass direction - d
# user's coordinates: (2,-1)
# pass direction - w
# user's coordinates: (2,0)
# pass direction - a
# user's coordinates: (1,0)
# pass direction - asd
# wrong string passed
# pass direction - a
# user's coordinates: (0,0)
# home reached

ux = int(input("pass user x coordinate - "))
uy = int(input("pass user y coordinate - "))

moves = {'a': (-1, 0), 'w': (0, 1), 's': (0, -1), 'd': (1, 0)}
fin = False

while not fin:

	data = input("pass direction - ")
	if data in moves.keys():

		ux += moves[data][0]
		uy += moves[data][1]
		print("user's coordinates: (" + str(ux)+","+str(uy)+ ")")

		if ux == 0 and uy == 0:
			fin = True
			print("home reached")

	elif data == 'x':
		print("quitting")
		fin = True

	else:
		print("wrong string passed")
