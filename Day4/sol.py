def respect_common_rules(num):
	#6-digit code
	if len(num) != 6:
		return False

	#Never decreasing
	for i in range(len(num)-1):
		if num[i] > num[i+1]:
			return False

	return True

def respect_rules(num):
	#Has a double
	for i in range(len(num)-1):
		if num[i] == num[i+1]:
			break
	else:
		return False
	return True

def respect_rules2(num):
	l = []
	for i in range(5):
		x = num[i] == num[i+1] #There is a double
		if i != 0:
			x = x and num[i-1] != num[i] #Previous is not the same
		if i != 4:
			x = x and num[i+1] != num[i+2] #The digit after is not the same
		l.append(x)

	return any(l) #If there is any matching double...

nums = range(273025,767253)
nums = filter(respect_common_rules, map(str, nums))
print 'Answer:', len(filter(respect_rules, nums))
print 'Answer2:', len(filter(respect_rules2, nums))
