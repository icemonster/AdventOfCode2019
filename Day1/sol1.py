with open('input.txt') as f:
	data = f.read().split('\n')[:-1]

print sum(map(lambda x: int(x)//3-2, data))