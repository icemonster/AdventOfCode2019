from z3 import *

with open('input.txt') as f:
	inp = f.read().split('\n')

implies = []
stars = {}
for i in inp:
	n1, n2 = i.split(')')
	b1, b2 = n1,n2
	n1, n2 = Bool(n1), Bool(n2)
	implies.append(Implies(n2,n1))
	stars[b1], stars[b2] = n1, n2
	
s = Optimize()
s.add(implies)

for star in stars:
	s.add_soft(stars[star] == False)

total = 0
for star in stars:
	s.push()
	s.add(stars[star]) #What if star is True?
	assert s.check() == sat 
	m = s.model()

	#How many stars would necessarily have to be True?
	answer = [m[stars[i]].__bool__() for i in stars if m[stars[i]] is not None]
	total += sum(answer) - 1 #Dont count with the star itself
	s.pop()

print total