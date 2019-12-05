code = [3,225,1,225,6,6,1100,1,238,225,104,0,101,20,183,224,101,-63,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1101,48,40,225,1101,15,74,225,2,191,40,224,1001,224,-5624,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,62,60,225,1102,92,15,225,102,59,70,224,101,-885,224,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,35,188,224,1001,224,-84,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,66,5,224,1001,224,-65,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1002,218,74,224,101,-2960,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,49,55,224,1001,224,-104,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1102,43,46,225,1102,7,36,225,1102,76,30,225,1102,24,75,224,101,-1800,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,43,40,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,479,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,554,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,644,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]

class Immediate:
    def __getitem__(self, key):
        return key

def add(machine, modes, ip):
	x = machine[ip+1]
	y = machine[ip+2]
	dst = machine[ip+3]

	#Modes
	x = modes[2][x]
	y = modes[1][y]
	
	machine[dst] = x + y

def mul(machine, modes, ip):
	x = machine[ip+1]
	y = machine[ip+2]
	dst = machine[ip+3]

	x = modes[2][x]
	y = modes[1][y]
	
	machine[dst] = x * y

def inp(machine, modes, ip):
	dst = machine[ip+1]
	x = int(raw_input())
	machine[dst] = x

def out(machine, modes, ip):
	o = machine[ip+1]
	o = modes[0][o]
	print o


def jmp(machine, modes, _, cond):
	global ip
	x = machine[ip+1]
	y = machine[ip+2]

	x = modes[1][x]
	newIP = modes[0][y]

	if cond(x):
		ip = newIP - 3 #IP will increment 3 units after this OPcode automatically

def condStore(machine, modes, ip, cond):
	x = machine[ip+1]
	y = machine[ip+2]
	dst = machine[ip+3]

	x = modes[2][x]
	y = modes[1][y]
	
	toStore = 0
	if cond(x,y):
		toStore = 1

	machine[dst] = toStore

ADD, MUL, INP, OUT, JT, JF, LT, EQ = range(1,9)

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

ip = 0
while code[ip] != 99:
	nextOP = code[ip]

	func = int(str(nextOP)[-2:])
	sz, func = opcodes[func]
	modes = str(nextOP)[:-2].zfill(sz)

	modes = map(lambda x: modes_op[x], modes)
	func(code, modes, ip)
	ip += (sz+1) #Instr len = number of parameters + 1 (opcode)
