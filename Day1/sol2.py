with open('input.txt') as f:
	data = f.read().split('\n')[:-1]

data = map(int, data)
def compute_fuel(m):
	return max(m//3-2,0)

total = 0
size = len(data)
while data != [0]*size:
	data = map(compute_fuel, data)
	total += sum(data)

print total