code = [3,8,1005,8,311,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,28,1,1104,0,10,1006,0,71,2,1002,5,10,2,1008,5,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,66,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,87,1006,0,97,2,1002,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,116,1006,0,95,1,1009,10,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,145,1,1002,19,10,2,1109,7,10,1006,0,18,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,179,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,200,1,1105,14,10,1,1109,14,10,2,1109,11,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,235,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,257,2,101,9,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,282,2,1109,19,10,1,105,0,10,101,1,9,9,1007,9,1033,10,1005,10,15,99,109,633,104,0,104,1,21102,937268368140,1,1,21102,328,1,0,1106,0,432,21102,1,932700599052,1,21101,0,339,0,1105,1,432,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,209421601831,1,21102,1,386,0,1106,0,432,21102,235173604443,1,1,21102,1,397,0,1106,0,432,3,10,104,0,104,0,3,10,104,0,104,0,21101,825439855372,0,1,21102,1,420,0,1106,0,432,21101,0,988220907880,1,21102,431,1,0,1106,0,432,99,109,2,22101,0,-1,1,21101,40,0,2,21102,1,463,3,21102,453,1,0,1106,0,496,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,458,459,474,4,0,1001,458,1,458,108,4,458,10,1006,10,490,1102,1,0,458,109,-2,2106,0,0,0,109,4,2102,1,-1,495,1207,-3,0,10,1006,10,513,21102,0,1,-3,22102,1,-3,1,21202,-2,1,2,21102,1,1,3,21101,532,0,0,1105,1,537,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,560,2207,-4,-2,10,1006,10,560,21201,-4,0,-4,1106,0,628,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,579,0,1106,0,537,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,598,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,620,21201,-1,0,1,21102,1,620,0,105,1,495,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]

grid = {}
currentPos = 0 #random pos
grid[currentPos] = 1
imag = 1j
direction = -1j #Facing up
next_out_is_rot = False

relative_base = 0
class Immediate:
    def __getitem__(self, key):
        return key

class Relative:
	def __init__(self, code):
		self.code = code
	def __getitem__(self, key):
		global relative_base
		return self.code[key + relative_base]

class writableRelative:
	def __getitem__(self, key):
		global relative_base
		return key + relative_base

def getParam(machine, modes, ip, writable=True):
	if writable: #If last parameter is writable, its mode must not be 0
		if isinstance(modes[0], Relative):
			modes[0] = writableRelative()
		else:
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

def adj(machine, modes, ip):
	global relative_base
	x = getParam(machine, modes, ip, writable=False)[0]
	relative_base += x

def mul(machine, modes, ip):
	x,y,dst = getParam(machine, modes, ip)
	machine[dst] = x * y

def inp(machine, modes, ip):
	dst = getParam(machine, modes, ip)[0]
	machine[dst] = grid.get(currentPos) if grid.get(currentPos) is not None else 0

def out(machine, modes, ip):
	global next_out_is_rot, currentPos, direction
	o = machine[ip+1]
	o = modes[0][o]
	if not next_out_is_rot:
		grid[currentPos] = o
	else:
		if o == 1:
			direction = direction * imag
		else:
			direction = direction * (-imag)
		currentPos = currentPos + direction

	next_out_is_rot = not next_out_is_rot

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
ADD, MUL, INP, OUT, JT, JF, LT, EQ, ADJ = range(1,10)

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
opcodes[ADJ]  = (1, adj)

code = code + [0]*1000000

modes_op = {'0': code, '1':Immediate(),'2':Relative(code)}

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

runCode(code)

print 'answer1:',len(grid)

for i in range(6):
	s = ''
	for k in range(40):
		if k+i*1j not in grid or grid[k+i*1j] == 0:
			s += '.'
		else:
			s += '#'
	print s
