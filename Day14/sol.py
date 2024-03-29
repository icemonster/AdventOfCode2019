class Reaction:
	def __init__(self):
		self.inputs = []
		self.outputs = []
	def addInput(self, name, quantity):
		self.inputs.append((name, quantity))
	def addOutput(self, name, quantity):
		self.outputs.append((name, quantity))
	def hasInput(self, name):
		for inp in self.inputs:
			if inp[0] == name:
				return True
		return False
	def hasOutput(self, name):
		for out in self.outputs:
			if out[0] == name:
				return True
		return False
	def getInpQuantity(self, name):
		for inp in self.inputs:
			if inp[0] == name:
				return inp[1]
		assert False
	def getOutQuantity(self, name):
		for out in self.outputs:
			if out[0] == name:
				return out[1]
		assert False
	def __repr__(self):
		s = ''
		for inp in self.inputs:
			s += str(inp[1])+' '+inp[0]+','
		s = s[:-1]
		s += ' => '
		for out in self.outputs:
			s += str(out[1])+' '+out[0]+','
		return s[:-1]

def parseLine(line):
	r = Reaction()
	inps, outs = line.split('=>')
	inps = inps.split(',')
	outs = outs.split(',')
	for inp in inps:
		inp = inp.strip().split(' ')
		quant, name = inp
		r.addInput(name, int(quant))
	for out in outs:
		out = out.strip().split(' ')
		quant, name = out
		r.addOutput(name, int(quant))
	return r

with open('input.txt') as f:
	data = f.read()

data = data.split('\n')[:-1]

reactions = []
for i in data:
	reactions.append(parseLine(i))

def getReactionWithOut(name):
	return filter(lambda x:x.hasOutput(name), reactions)[0]

need = {'FUEL':1} #Compunds needed
while any(map(lambda x: x != 'ORE' and need[x] > 0 , need.keys())):
	for c in need.keys():
		needed = need[c]
		if needed > 0:
			if c == 'ORE': continue
			r = getReactionWithOut(c)
			q = r.getOutQuantity(c)
			mul = needed // q #how many times must we perform that reaction
			if mul*q < needed:
				mul += 1

			need[c] = needed - mul*q #We have spare stuff now possibly
			#But we need the inputs
			for inp in r.inputs:
				name, quant = inp
				if name in need:
					need[name] += quant*mul
				else:
					need[name] = quant*mul


print 'answer 1:', need['ORE']
#The quantity of Ore in needed is an upperbound. lets get the exact value
