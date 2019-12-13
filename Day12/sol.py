import ast
from Crypto.Util.number import GCD

class Moon:
	def __init__(self, t):
		self.x = t[0]
		self.y = t[1]
		self.z = t[2]
		self.vx, self.vy, self.vz = 0,0,0
	def potentialEne(self):
		return abs(self.x) + abs(self.y) + abs(self.z)
	def kineticEne(self):
		return abs(self.vx) + abs(self.vy) + abs(self.vz)
	def applyGravity(self, m): #Ugly as hell
		if self.x < m.x:
			self.vx += 1
		elif self.x > m.x:
			self.vx += -1
		if self.y < m.y:
			self.vy += 1
		elif self.y > m.y:
			self.vy += -1
		if self.z < m.z:
			self.vz += 1
		elif self.z > m.z:
			self.vz += -1
	def applyVelocity(self):
		self.x += self.vx
		self.y += self.vy
		self.z += self.vz
	def copy(self):
		m = Moon((self.x, self.y, self.z))
		m.vx,m.vy,m.vz = self.vx, self.vy, self.vz
		return m
	def __repr__(self):
		return 'pos=' + str((self.x, self.y, self.z)) + ', vel=' + str((self.vx, self.vy, self.vz)) 


def computeStep(moons):
	res = []
	for moon in moons:
		m = moon.copy()
		for moon2 in moons:
			m.applyGravity(moon2)
		m.applyVelocity()
		res.append(m)
	return res

def computeMoonEnergy(moon):
	return moon.potentialEne() * moon.kineticEne()

NRSTEPS = 1000

with open('input.txt') as f:
	data = f.read().split('\n')[:-1]

moons = []
for line in data:
	line = line.replace('<x=','').replace('y=','').replace('z=','').replace('>','')
	line = '(' + line + ')'
	line = ast.literal_eval(line)
	line = Moon(line)
	moons.append(line)

originalMoons = [i.copy() for i in moons]

for step in range(1000):
	moons = computeStep(moons)
print sum(map(computeMoonEnergy, moons))

def findRepeatingAxis(originalMoons, func):
	moons = [i.copy() for i in originalMoons] #Restore backup

	steps = 1
	while 1:
		moons = computeStep(moons)
		for moon in range(len(moons)):
			if not func(moons, originalMoons, moon):
				break
		else:
			return steps
		steps += 1


findX = lambda m, orig, i: m[i].x == orig[i].x and m[i].vx == orig[i].vx
findY = lambda m, orig, i: m[i].y == orig[i].y and m[i].vy == orig[i].vy
findZ = lambda m, orig, i: m[i].z == orig[i].z and m[i].vz == orig[i].vz

x = findRepeatingAxis(originalMoons, findX)
y = findRepeatingAxis(originalMoons, findY)
z = findRepeatingAxis(originalMoons, findZ)

def lcm(x,y):
	return x*y // GCD(x,y)

print reduce(lcm, [x,y,z])