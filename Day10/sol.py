from Crypto.Util.number import GCD
from math import *

def priority(center, line):
	eq = (line[0]-center[0], line[1]-center[1])
	return -(degrees(atan2(eq[0], eq[1]))+180) % 360

def normalize(line):
	a = GCD(line[0], line[1])
	return (line[0]//a, line[1]//a)

def compute_eqs(asteroid, asteroids):
	lines = []
	for a in asteroids:
		line = (a[0]-asteroid[0], a[1]-asteroid[1])
		lines.append(normalize(line))
	return lines

def compute_detectable(asteroid, asteroids):
	return len(set(compute_eqs(asteroid, asteroids)))

asteroids = []

#Parse asteroids
with open('input.txt') as f:
	data = f.read().split('\n')[:-1]
	for line in range(len(data)):
		for col in range(len(data[line])):
			if data[line][col] == '#':
				asteroids.append((col, line))

#Compute best location for monitoring station
m = 0
asteroid = None
for a in asteroids:
	v = compute_detectable(a, [i for i in asteroids if i != a])
	if v > m:
		m = v
		asteroid = a

print 'answer first:', m

#Sort asteroids by degree relative to center
asteroids.remove(asteroid)
asteroids.sort(key=lambda x: priority(asteroid, x))

lines = compute_eqs(asteroid, asteroids)

for total in range(200):
	e = lines.pop(0)
	a = asteroids.pop(0)
	while lines[0] == e: #Ignore remaining asteroids in the same line
		e = lines.pop(0)
		a = asteroids.pop(0)
		lines.append(e)
		asteroids.append(a)

print 'answer second:', a