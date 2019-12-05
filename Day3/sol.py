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

pnts1_1 = getAllCoords(wire1)
pnts2_1 = getAllCoords(wire2)

pnts1 = set(pnts1_1)
pnts2 = set(pnts2_1)

inters = pnts1 & pnts2

best = float('inf')
for pnt in inters:
	x = pnts1_1.index(pnt) + pnts2_1.index(pnt) + 2
	best = min(best, x)

print 'answer1:', min(map(manhattan, inters))
print 'answer2:', best