with open('input.txt') as f:
	wire1 = f.readline().strip().split(',')
	wire2 = f.readline().strip().split(',')

def manhattan(pnt):
	return abs(pnt[0]) + abs(pnt[1])

def getAllCoords(wire):
	pntsWire = []
	currentPosition = (0,0)
	for i in wire:
		direction = i[0]
		if direction == 'R':
			direction = (1,0)
		elif direction == 'L':
			direction = (-1,0)
		elif direction == 'U':
			direction = (0, 1)
		else:
			direction = (0, -1)

		nr = int(i[1:])
		for j in range(nr):
			currentPosition = (currentPosition[0] + direction[0], currentPosition[1] + direction[1])
			pntsWire.append(currentPosition)

	return pntsWire

pnts1 = set(getAllCoords(wire1))
pnts2 = set(getAllCoords(wire2))

inters = pnts1 & pnts2

best = float('inf')

for pnt in inters:
	x = manhattan(pnt)
	if x < best:
		best = x

print 'answer:', best