remember = []
def minimum(s1, lst):
	''' Compute minimum distance between s1 and SAN '''
	if s1 not in remember:
		remember.append(s1)
	else: return float('inf')

	if [s1, "SAN"] in lst or ["SAN", s1] in lst: return 1

	distances =  [minimum(i[0], lst) for i in lst if i[1] == s1]
	distances += [minimum(i[1], lst) for i in lst if i[0] == s1]

	if distances == []: return float('inf')
	else:				return min(distances) + 1


with open('input.txt') as f:
	lst = [i.split(')') for i in f.read().split('\n')]

print minimum('YOU', lst) - 2