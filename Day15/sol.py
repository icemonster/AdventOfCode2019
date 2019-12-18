from queue import Queue 

code = [3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,101,0,1034,1039,101,0,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,102,1,1034,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,1002,1035,1,1040,1002,1038,1,1043,1001,1037,0,1042,1105,1,124,1001,1034,1,1039,1008,1036,0,1041,1002,1035,1,1040,101,0,1038,1043,101,0,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,35,1032,1006,1032,165,1008,1040,33,1032,1006,1032,165,1102,2,1,1044,1106,0,224,2,1041,1043,1032,1006,1032,179,1101,1,0,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,27,1044,1105,1,224,1101,0,0,1044,1105,1,224,1006,1044,247,101,0,1039,1034,1002,1040,1,1035,101,0,1041,1036,1001,1043,0,1038,101,0,1042,1037,4,1044,1106,0,0,8,86,20,11,8,18,84,20,96,25,15,28,96,20,74,24,7,5,77,6,77,6,23,74,3,23,93,21,72,23,1,57,87,10,17,9,23,48,16,9,32,11,62,73,5,70,2,10,77,23,16,76,24,28,13,46,92,26,15,10,87,13,28,54,10,50,4,16,47,75,24,55,4,99,92,17,66,24,7,13,33,43,21,65,24,4,74,40,8,28,25,5,72,25,5,54,19,72,6,44,49,3,65,11,24,85,39,11,5,77,15,6,65,12,66,66,14,8,88,81,2,8,99,7,54,70,2,97,69,9,17,51,47,1,56,88,81,41,10,98,16,23,35,24,82,24,5,99,39,67,8,14,46,56,5,8,59,9,53,9,21,95,6,95,7,12,85,26,79,82,19,21,62,99,5,13,81,19,31,15,29,67,45,22,75,84,14,25,83,33,97,4,85,15,17,25,21,51,55,11,76,32,15,43,60,13,13,11,65,65,16,9,96,26,17,10,94,23,12,37,16,49,2,81,17,11,20,17,16,37,87,16,12,96,23,10,68,22,75,34,4,22,14,34,14,62,8,34,12,72,7,40,5,54,10,89,7,96,1,14,72,7,11,60,93,68,51,21,86,25,34,26,20,38,7,21,94,78,10,8,46,4,81,12,84,30,11,9,48,12,83,73,42,83,26,26,40,22,91,6,38,99,2,40,24,93,10,22,84,22,19,94,8,6,42,33,11,15,31,66,33,2,65,39,67,26,5,67,19,86,1,12,20,28,54,80,84,3,17,32,26,51,8,6,20,67,15,54,30,5,31,97,9,10,29,18,45,8,23,69,18,61,11,4,73,5,46,13,96,16,80,66,17,1,11,50,37,4,34,94,15,32,77,5,93,69,12,66,6,24,18,84,26,42,5,78,74,22,82,15,23,60,11,64,61,59,48,11,99,49,3,68,2,16,14,99,7,94,9,22,75,20,30,21,17,91,20,41,21,26,42,44,19,18,85,17,96,21,2,88,62,69,8,39,3,11,62,12,25,29,69,79,52,56,6,52,22,78,42,8,18,22,59,91,13,94,89,10,16,73,11,17,80,81,26,36,26,55,16,13,30,6,6,43,1,43,83,21,69,11,42,8,77,21,31,25,24,99,26,56,85,15,74,1,88,13,3,18,42,14,54,13,6,91,49,7,36,42,2,8,67,55,14,35,5,33,6,96,24,94,24,59,46,18,4,61,95,2,33,33,2,31,24,97,1,91,15,52,15,53,44,10,20,47,93,8,1,48,80,22,80,23,15,92,18,18,59,19,69,17,8,55,38,26,9,68,23,85,2,12,23,77,4,21,16,6,90,45,17,61,16,28,22,24,58,30,26,2,85,1,53,29,18,37,30,38,4,12,92,60,19,13,56,19,85,7,66,19,73,39,9,90,81,3,8,9,72,25,37,24,5,96,25,13,81,92,34,19,95,3,26,36,25,25,25,15,95,6,35,43,92,10,79,70,8,30,18,96,75,1,5,76,17,86,3,46,22,11,50,96,1,56,43,2,23,53,7,71,20,61,73,34,31,57,24,69,4,24,6,25,98,50,21,63,12,97,11,9,72,19,40,21,7,2,18,77,83,16,1,82,24,25,57,72,25,9,15,76,21,14,71,16,94,7,64,21,69,87,18,65,1,21,20,61,91,10,86,7,55,36,1,40,99,39,8,41,5,92,76,33,20,40,15,81,76,48,5,35,64,59,6,30,13,52,19,84,21,58,1,89,29,53,10,76,22,33,26,65,3,96,0,0,21,21,1,10,1,0,0,0,0,0,0]

grid = {}

def showGrid(grid):
	for row in range(100):
		s = ''
		for col in range(100):
			if (col,row) in grid:
				if grid[(col,row)] == 0:
					s += '#'
				elif grid[(col,row)] == 1:
					s += '.'
				elif grid[(col,row)] == 2:
					s += 'O'
				else:
					s += ' '
			else:
				s += ' '
		print(s)

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
	global input_to_pass
	dst = getParam(machine, modes, ip)[0]
	machine[dst] = input_to_pass

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

code = code + [0]*10000

def runCode(code, ip_start=0):
	global ip
	ip = ip_start
	modes_op = {'0': code, '1':Immediate(),'2':Relative(code)}


	while code[ip] != 99:
		nextOP = code[ip]
		sz, func = opcodes[nextOP%100]
		modes = str(nextOP)[:-2].zfill(sz)
		modes = list(map(lambda x: modes_op[x], modes))

		out = func(code, modes, ip)
		ip += (sz+1) #Instr len = number of parameters + 1 (opcode)

		if out is not None:
			return out
		
NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

def goDir(pos, dire):
	if dire == NORTH:
		pos = (pos[0], pos[1]-1)
	elif dire == SOUTH:
		pos = (pos[0], pos[1]+1)
	elif dire == WEST:
		pos = (pos[0]-1, pos[1])
	elif dire == EAST:
		pos = (pos[0]+1, pos[1])
	else:
		assert False, "Invalid direction"
	return pos

def addChild(states, seen, state, dire):
	global input_to_pass
	global ip

	ip, code, pos, depth = state

	pos = goDir(pos, dire)
	if pos not in seen:
		depth += 1
		code = [i for i in code] #Copy code
		input_to_pass = dire
		out = runCode(code, ip)
		grid[pos] = out
		if out != 0:
			states.put((ip, code, pos, depth))
		seen[pos] = True
		return out

seen = {(50,50):True}
initialState = (0, [i for i in code], (50,50),0) #IP, code+mem, currentPos, depth
states = Queue()
states.put(initialState)

#First BFS
while not states.empty():
	state = states.get()
	for dire in (NORTH, SOUTH, WEST,EAST):
		if addChild(states, seen, state, dire) == 2:
			print('Answer 1:', state[-1])

for i in grid: #Find oxygen
	if grid[i] == 2:
		ox = i
		break

states.put((ox, 0))
seen = {ox:True}

#Second BFS
while not states.empty():
	state, depth = states.get()
	for dire in (NORTH, SOUTH, WEST,EAST):
		pos2 = goDir(state, dire)
		if pos2 not in seen:
			seen[pos2] = True
			if pos2 in grid and grid[pos2] == 1:
				states.put((pos2, depth+1))

print('Answer 2:', depth)