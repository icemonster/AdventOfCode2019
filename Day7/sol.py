import itertools

code = [3,8,1001,8,10,8,105,1,0,0,21,42,67,76,89,110,191,272,353,434,99999,3,9,102,2,9,9,1001,9,2,9,1002,9,2,9,1001,9,2,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,101,3,9,9,1002,9,2,9,1001,9,4,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,102,3,9,9,101,2,9,9,1002,9,3,9,101,5,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]


class Immediate:
    def __getitem__(self, key):
        return key

def getParam(machine, modes, ip, writable=True):
	if writable: #If last parameter is writable, its mode must not be 0
		modes[0] = Immediate()

	params = []
	nr = len(modes)
	for i in range(nr):
		param = machine[ip + 1 + i]
		params.append(modes[nr - i - 1][param])

	return params


def add(machine, modes, ip):
	x,y,dst = getParam(machine, modes, ip)
	machine[dst] = x + y

def mul(machine, modes, ip):
	x,y,dst = getParam(machine, modes, ip)
	machine[dst] = x * y

def inp(machine, modes, ip):
	global provided
	dst = machine[ip+1]
	#machine[dst] = int(raw_input())
	if not provided:
		machine[dst] = give_input
		provided = True
	else:
		machine[dst] = give_input2

def out(machine, modes, ip):
	o = machine[ip+1]
	o = modes[0][o]
	return o

def jmp(machine, modes, _, cond):
	global ip
	x,newIP = getParam(machine, modes, ip, writable=False)
	if cond(x):
		ip = newIP - 3 #IP will increment 3 units after this OPcode automatically

def condStore(machine, modes, ip, cond):
	x,y,dst = getParam(machine, modes, ip)
	
	toStore = 0
	if cond(x,y):
		toStore = 1

	machine[dst] = toStore

#Greatest way to get an enumerate
ADD, MUL, INP, OUT, JT, JF, LT, EQ = range(1,9)

#Most abstract code ever made
diffTZero = lambda x: x != 0
eqZero = lambda x: x == 0
eq = lambda x,y: x == y
lt = lambda x,y: x < y

opcodes = {} #Nr of parameters of each opcode
opcodes[ADD] = (3, add)
opcodes[MUL] = (3, mul)
opcodes[INP] = (1, inp)
opcodes[OUT] = (1, out)
opcodes[JT]  = (2, lambda machine,modes,ip: jmp(machine, modes, ip, diffTZero))
opcodes[JF]  = (2, lambda machine,modes,ip: jmp(machine, modes, ip, eqZero))
opcodes[LT]  = (3, lambda machine,modes,ip: condStore(machine, modes, ip, lt))
opcodes[EQ]  = (3, lambda machine,modes,ip: condStore(machine, modes, ip, eq))

modes_op = {'0': code, '1':Immediate()}

def runCode(code):
	global ip
	ip = 0
	while code[ip] != 99:
		nextOP = code[ip]

		sz, func = opcodes[nextOP%100]
		modes = str(nextOP)[:-2].zfill(sz)
		modes = map(lambda x: modes_op[x], modes)

		out = func(code, modes, ip)
		if out is not None:
			return out
		ip += (sz+1) #Instr len = number of parameters + 1 (opcode)

outs = []
for comb in itertools.permutations([0,1,2,3,4]):
	give_input2 = 0
	for give_input in comb:
		provided = False
		give_input2 = runCode(code)
	outs.append(give_input2)

print max(outs)