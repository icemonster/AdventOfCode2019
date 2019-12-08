with open('input.txt') as f:
	data = f.read().strip()

size_im = 25 * 6
layers = [data[i:i+size_im] for i in range(0, len(data), size_im)]

bestVal = float('inf')
best = None

for layer in layers:
	if layer.count('0') < bestVal:
		bestVal = layer.count('0')
		best = layer.count('1')*layer.count('2')

print best