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

print('Answer1:', best )

finalLayer = ''
for i in range(150):
	cur = '2'
	for layer in layers:
		if cur == '2':
			cur = layer[i]
	finalLayer += cur

finalLayer = finalLayer.replace('0',' ')
for i in range(0,len(finalLayer), 25):
	print(finalLayer[i:i + 25])
