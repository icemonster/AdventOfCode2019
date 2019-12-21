inp = map(int, '59790132880344516900093091154955597199863490073342910249565395038806135885706290664499164028251508292041959926849162473699550018653393834944216172810195882161876866188294352485183178740261279280213486011018791012560046012995409807741782162189252951939029564062935408459914894373210511494699108265315264830173403743547300700976944780004513514866386570658448247527151658945604790687693036691590606045331434271899594734825392560698221510565391059565109571638751133487824774572142934078485772422422132834305704887084146829228294925039109858598295988853017494057928948890390543290199918610303090142501490713145935617325806587528883833726972378426243439037')
originalPat = [0, 1, 0, -1]


def doPhase(inp):
	out = []
	for i in range(1, len(inp)+1):
		pat = []
		for p in originalPat:
			for j in range(i):
				pat.append(p)

		pat = pat * (len(inp)/len(pat)+1)
		pat = pat[1:] #skip the very first value exactly once.

		s = 0
		for j in range(len(inp)):
			s += inp[j]*pat[j]
		out.append(abs(s) % 10)
	return out

inp2 = [i for i in inp]
for i in range(1):
	inp2 = doPhase(inp2)
print 'Answer 1:', inp2[:8]

def fastDoPhase(inp):
	inp2 = []
	s = 0
	for i in inp:
		s += i
		inp2.append(s % 10)
	return inp2

inp = inp * 10000
#Last digit have pattern full of zeros except a one. As we go from right to left, the number of ones increase and therefore we sum more digits
offset = int(''.join(map(str, inp[:7])))
inp = inp[offset:]
inp = inp[::-1]
for i in range(100):
	inp = fastDoPhase(inp)

print 'Answer 2:', inp[::-1][:8]